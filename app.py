from wsgiref.handlers import read_environ
from flask import Flask, render_template, request
import os
from PIL import Image



app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/form', methods=['GET','POST'])
def mnist():
    if request.method == 'GET' :
        return render_template('form.html')
    else :
        # request.files[' "form.html의 input태그의 name값" ']
        f = request.files['mnist_input']
        # os.path.dirname(__file__) 는 현재 파일의 경로
        path = os.path.dirname(__file__)+'/upload/' + f.filename
        f.save(path)

        return '성공!!' # 결과 확인용 return


if __name__ == '__main__' :
    app.run(debug=True)
