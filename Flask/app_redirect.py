from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')    #<guest> : guest 쪽에 값이 넘어 오기 때문에 밑에 메소드에 파라미터로 값을 넣어줘야한다.
def hello_guest(guest):
    return 'Hello %s as Guest' %guest

@app.route("/user/<name>")
def hell_user(name):
    if name == 'admin':
#        return redirect(url_for('hello_admin')) # url_for 안에는 메소드명을 넣어준다. 아래의 방법도 된다.
        return redirect('/admin')  
    else:
        return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__': 
    app.run()