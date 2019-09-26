# simple echo server

import socket

def run_server(host="127.0.0.1", port=4000):
    with socket.socket() as s:
        s.bind((host,port))
        s.listen(1)
        conn, addr = s.accept()
        msg = conn.recv(1024)
        print(f'{msg.decode()}')
        conn.sendall(msg)
        conn.close()

if __name__ == '__main__':
    run_server()