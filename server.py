import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 1234
        s = socket.socket()
    except socket.error as msg:
        print('Socket cant be created !' + str(msg))


def bind_socket():
    try:
        s.bind((host, port))
        print('Socket binding done')
        s.listen(5)
        print('Now listening at port {}.....'.format(port))
    except socket.error as msg:
        print('Socket binding failed! ' + str(msg) + '\nRetrying...')
        print('retry')
        bind_socket()


def accept_socket():
    c, a = s.accept()
    print('Connection established with ' + a[0])
    send_commands(c)
    c.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(cmd) > 0:
            conn.send(str.encode(cmd))
            response = str(conn.recv(1024), 'utf-8')
            print(response, end='')     # default end='' means end='\n'


def main():
    create_socket()
    bind_socket()
    accept_socket()

main()



