import socket
 
HOST = '192.168.0.159'
PORT = 8888
 
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
        with open('/Users/Shinwoohyun/' + filename, 'wb') as f:
            try:
                while  data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)
 
    print('파일[%s] 전송종료. 전송량 [%d]' %(filename, data_transferred))
 
filename = input('다운로드 받은 파일이름을 입력하세요:')
getFileFromServer(filename)

