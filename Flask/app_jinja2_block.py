from flask import Flask, render_template

# jinja2 의 장점중 하나는 상속이 가능하기 때문에 html 파일중 똑같은 웹 코드가 반복되야 하는 것은 상속을 통해서 해결 할 수 있다.ㄹ
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

if __name__=='__main__':
    app.run()