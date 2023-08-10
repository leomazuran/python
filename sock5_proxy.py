import socket
import select
import threading

def handle_client(client_socket):
    try:
        # Receive the initial connection request from the client
        version, nmethods = client_socket.recv(2)
        client_socket.recv(nmethods)

        # Respond with the method selection (No authentication required)
        response = b'\x05\x00'
        client_socket.sendall(response)

        # Request and process the target address and port
        version, cmd, _, address_type = client_socket.recv(4)
        if cmd != 0x01:  # Only support CONNECT command
            client_socket.close()
            return

        if address_type == 0x01:  # IPv4
            target_address = socket.inet_ntoa(client_socket.recv(4))
        elif address_type == 0x04:  # IPv6
            target_address = socket.inet_ntop(socket.AF_INET6, client_socket.recv(16))
        else:  # domain name
            addr_len = int.from_bytes(client_socket.recv(1), byteorder='big')
            target_address = client_socket.recv(addr_len).decode('utf-8')

        target_port = int.from_bytes(client_socket.recv(2), byteorder='big')

        # Connect to the target server
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((target_address, target_port))

        # Respond to the client that the connection is established
        response = b'\x05\x00\x00\x01\x00\x00\x00\x00\x00\x00'
        client_socket.sendall(response)

        # Start forwarding data between client and target
        forward_data(client_socket, target_socket)
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()
        target_socket.close()

def forward_data(src_socket, dest_socket):
    try:
        while True:
            rlist, _, _ = select.select([src_socket, dest_socket], [], [], 5)
            if src_socket in rlist:
                data = src_socket.recv(4096)
                if not data:
                    break
                dest_socket.sendall(data)
            if dest_socket in rlist:
                data = dest_socket.recv(4096)
                if not data:
                    break
                src_socket.sendall(data)
    except Exception as e:
        print("Error:", e)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("SOCKS5 server listening on 0.0.0.0:8080")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
