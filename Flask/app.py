from flask import Flask, render_template, request

app = Flask(__name__)

# request 라는 객체에 클라이언트의 요구사항을 다 담아서 서버측에 보낸다.
# response 객체에 담아서 서버는 클라이언트에게 다시 돌려보낸다. 
@app.route('/')
def index():    # 함수의 이름은 @app.route('...') ...의 값과 최대한 맞춘다. 어떠한 이름이든 가능하나 중복은 안된다.
    return render_template("index.html")

@app.route('/Page_Endgame.html')
def Page_Endgame():
    return render_template("Page_Endgame.html")

@app.route('/Page_Money.html')
def Page_Money():
    return render_template("Page_Money.html")

@app.route('/Page_Parasite.html')
def Page_Parasite():
    return render_template("Page_Parasite.html")

@app.route('/Movie_Project.html')
def Movie_Project():
    return render_template("Movie_Project.html")

@app.route('/Crytocurrency_Project.html')
def Crytocurrency_Project():
    return render_template("Crytocurrency_Project.html")

@app.route('/Contact.html')
def Contact():
    return render_template("Contact.html")

@app.route('/Project_Outline.html')
def Project_Outline():
    return render_template("Project_Outline.html")

################### 여기까지는 나의 홈페이지 내용 #############33

@app.route('/user/<getvalue>') # 값을 저장할 변수명 getvalue
def user(getvalue):
    return 'user %s' %getvalue

@app.route('/user/<getvalue>/<int:age>')
def user2(getvalue,age):
    return 'username %s, 나이 %d' %(getvalue,age)

@app.route('/user/<getvalueID>/<getvaluePW>')
def user3(getvalueID,getvaluePW):
    return render_template('test.html',ID=getvalueID ,PW=getvaluePW)
    # html안의 값(=ID,PW)은 앞에 놓고 route에서의 값은 뒤쪽에 놓는다.

@app.route('/forminput/')
def forminput():
    return render_template('test_form.html')

@app.route('/method/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"

@app.route('/login/')
def login1():
    username=request.args.get('name')      #확인 할 떄 : http://127.0.0.1:5000/login/?name=shin
    return render_template('test.html',ID=username)

@app.route('/forminput1/')
def forminput1():
    return render_template('test_form1.html')

@app.route('/login/', methods=['POST'])  #확인 할 떄 : http://127.0.0.1:5000/forminput1/
def login_post():                           # POST 방식은 {{}} 와 같은 jinja 폼으로 쓰고
    username=request.form['username']
    password=request.form['password']
    return render_template('test.html',ID=username, PW=password)


if __name__ == '__main__':  # 메인 파일에서만 실행시켜라 라고 조건문을 걸어주는 것이다. 만약 다른 파일에서 import Flask 를 메모리에 올려버리면 자동으로 줄줄 실행되기 때문이다.
    app.run()