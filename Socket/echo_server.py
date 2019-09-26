'''
개 어려움 쓰지마셈 --> 공부할때나 보기
'''
import socket
import pandas as pd

def run_server(host="192.168.0.183", port=7792):
    text =[[]]
    BUF_SIZE =1024
    with socket.socket() as sock:
        sock.bind((host,port))
        sock.listen()
        conn, addr = sock.accept()
        while True:
            # data = 인코딩 되어있는 데이터
            data = conn.recv(BUF_SIZE)

            # msg = data를 디코드 해서 사람이 이해할 수 있는 데이터
            msg = data.decode()

            text.append(data.decode())
            
            # 처리중 : str 자료형이기 때문에 int 형으로 바꿔주는 코드
            msg_int=int(msg)
            msg_int+=1
            msg = str(msg_int)
            print(msg)
            print(type(msg))

            # 처리후 : 데이터를 인코딩 하는 것
            data = msg.encode()
            conn.sendall(data)
            
            # 접속을 끊기 위한 메세지 & 로그
            if msg == 'bye':
                conn.close()
                dataframe = pd.DataFrame(text)
                dataframe.to_csv("/Users/Shinwoohyun/test1.csv",header=False, index=False)
                break

if __name__ == '__main__':
    run_server()