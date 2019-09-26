from flask import Flask, url_for

# 클라이언트에서 / 기준으로 request를 하는데 @에노테이션 안에 있는 "함수" 를 호출 하기위해서 url 을 사용한다.
app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login/')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

if __name__ == '__main__':
    with app.test_request_context():
        # url 주소값을 print해준다.
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('profile', username='shin'))

# redirect 
# 클라이언트가 A를 요청했다. 서버가 A를 처리 할 수 없고 B를 요청해야 한다. 따라서 서버가 클라이언트에게 B를 요청하라고 한다. 클라이언트가 B를 요청하고 서버가 처리해서 내려다 준다.
# 두번왔다 갔다 한게 보인다. 예시 ) 로그인시 DB에서 정보가 있는지 없는지 확인하고 로그인 성공 또는 실패 분기점 처리.

# 포워딩
# 클라이언트가 A를 요청했다. 서버가 A를 처리 할 수 없고 B를 요청해야 한다. 서버가 알아서 B를 처리하고 A의 결과 값만 내려다 보낸다.
# 한번만 보낸다.

