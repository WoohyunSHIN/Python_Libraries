응호 hdfs 에서 데이터를 들고올 때, 사용할 python 코드

> **가장 중요한 것은 필요한 port 를 다 열어야 하고 AWS에서는 ICMP도 port 를 열어서 사용해야 한다.**

SERVER in AWS EC2

```python
import socketserver
from os.path import exists
 
HOST = '' # 적을 필요없다. 어짜피 client 에서 들어온 request 로 socket tunel 을 뚫어 놓기 때문이다.
PORT = 9991 # 사용할 포트
 
class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s] 연결됨' %self.client_address[0])
        filename = self.request.recv(1024) # 클라이언트로 부터 파일이름을 전달받음
        filename = filename.decode() # 파일이름 이진 바이트 스트림 데이터를 일반 문자열로 변환
 
        if not exists(filename): # 파일이 해당 디렉터리에 존재하지 않으면
            return # handle()함수를 빠져 나온다.
 
        print('파일[%s] 전송 시작...' %filename)
        with open('/home/ubuntu/'+filename, 'rb') as f:
            try:
                data = f.read(1024) # 파일을 1024바이트 읽음
                while data: # 파일이 빈 문자열일때까지 반복
                    data_transferred += self.request.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)
 
        print('전송완료[%s], 전송량[%d]' %(filename,data_transferred))
 
 
def runServer():
    print('++++++파일 서버를 시작++++++')
    print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요.")
 
    try:
        server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++파일 서버를 종료합니다.++++++')
 
 
runServer()


```



CLIENT

```python
import socket
 
HOST = '3.19.28.88'
PORT = 9991
 
def getFileFromServer(filename):
    data_transferred = 0
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        sock.sendall(filename.encode())
        print(HOST)
        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' %filename)
            return
                # 파일 저장 위치 잡아주면 될듯
        with open('/Users/Shinwoohyun/' + filename, 'wb') as f: # 저장할 위치
            try:
                while  data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)
 
    print('파일[%s] 전송종료. 전송량 [%d]' %(filename, data_transferred))
 
filename = input('다운로드 받은 파일이름을 입력하세요:') #예를들어 a.txt
getFileFromServer(filename)

```

