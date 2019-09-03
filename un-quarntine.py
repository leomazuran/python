import sys 
input1 = ""
input2 = ""

q_folder = "C:\\ProgramData\\Sentinel\\Quarantine\\"
input1 = raw_input ("Quarantine File Name? example: 16D68206213A414980DAF8954F4494D6: ")
input2 = raw_input ("Dump Location? example: C:\\Users\\<username>\\Desktop\\filename.exe: ")

file(input2, 'wb').write(''.join([chr(ord(x) ^ 0xff) for x in file(q_folder+input1+".MAL", 'rb').read()]))
