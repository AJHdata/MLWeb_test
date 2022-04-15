from wsgiref.handlers import read_environ
from flask import Flask, render_template, request
import os

from PIL import Image
import pickle
import numpy as np


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

        # return '성공!!' # 결과 확인용 return

                # -----------------------------------------------------------
        # 이미지 수치화, convert 그레이로 스케일링
        img = Image.open(path).convert('L')
        # 흰색 검은색 반전시키기
        img = np.resize(img,(1,784))
        
        # 이미지 열기
        mpath = os.path.dirname(__file__) + '/model1.pickle'
        
        with open(mpath, 'rb') as f :
            model = pickle.load(f)
        
        pred = model.predict(img)

        # return '성공!!' + str(pred) # 결과 확인용 return
        return render_template('result.html', data=pred)
        # result.html 페이지로, data는 pred를 던져준다.
        # => result.html 페이지에서 작업한다.
        # 주의!!!! add 하기 전에 .gitignore 파일 작성해라!!
        # model1 파일 너무 커서 안올라감.
        

if __name__ == '__main__' :
    app.run(debug=True)
