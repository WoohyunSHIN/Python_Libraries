from flask import Flask, render_template, request
import os

app = Flask(__name__)

#파일 업로드를 어떻게 처리할 것인지 ?
@app.route('/fileform')
def fileform():    
    return render_template("test_file.html")

@app.route('/fileUpload', methods=['POST'])
def fileUpload():
    f = request.files['file']  # f라는 객체에 request에서 넘어온 file의 위치를 저장하고
    dirname = os.path.dirname(__file__) + '/upLoads/' + f.filename  # os라는 외장함수로 
    print(dirname)
    f.save(dirname)     # 서버 side에 저장시키기
    return "upload 성공 " 

if __name__ == '__main__': 
    app.run()