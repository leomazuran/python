import socket
import time
import datetime
while True:
#Connect to Port 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("IP ADDRESS HERE",PORT HERE))
    # if no connection issues, port is good and dump to txt file for logging.
    if result == 0:
        currentDT = datetime.datetime.now()
        f = open("C:\\Users\\leonardo.mazuran\\Desktop\\PortUPLog.txt", "a")
        f.write ("\nPort OPEN\n")
        f.write (str(currentDT))
        print (currentDT)
        print ("Port is open")
        f.close()
        time.sleep (30)
    else:
    # if can not connect. port is closed and send to txt file for logging. 
        currentDT = datetime.datetime.now()
        f = open("C:\\Users\\leonardo.mazuran\\Desktop\\PortUPLog.txt", "a")
        f.write ("\nPort CLOSED\n")
        f.write (str(currentDT))
        f.close()
        print (currentDT)
        print ("Port is not open")
        time.sleep (30)
