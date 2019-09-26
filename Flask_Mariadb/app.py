from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

# db table은 run() 할 떄 한번만 생성 시켜주는게 가장 좋다.
db.create_table()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insert', methods=['POST'])
def insert():
    # <form> 태그에서 넘어 오는 값을 dictionary로 바꾸고 result에다가 넣는다.
    # console 창을 보면 딕셔너리형식으로 찍히는 걸 볼 수 있다.
    user = request.form.to_dict()
    db.insert_users(list(user.values()))
    return redirect('/list') 

@app.route('/list')
def list_user():
    users=db.all_users()
    return render_template("list.html",users=users)

@app.route('/content/<userid>') # 여기서 userid 라는 것을 받아 왔기 때문에 무조건 userid를 파라미터로 받아야한다.
def content(userid):    
    user=db.one_user(userid)
    return render_template("content.html",user=user)

@app.route('/delete/<userid>')
def delete(userid):
    db.delete_users(userid)
    return redirect("/list")

@app.route('/modify1/<userid>')
def modify_1(userid):
    return render_template("modify2.html",userid=userid)

@app.route('/modify2', methods=['POST'])
def modify_2():
    user = request.form.to_dict()
    print(user)
    print(type(user))
    db.update_users(user)
    return redirect("/list")

if __name__ == '__main__': 
    app.run()
