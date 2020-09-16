from flask import Flask
from flask import render_template
from flask import redirect
import os
from flask import url_for
from flask import logging
from flask import flash
from flask import request
from flask import session
app=Flask(__name__)


@app.route('/')
def home():
    filenames = os.listdir('static/exam_cheater/')
    print(filenames)
    return render_template('home.html', filenames = filenames)

if __name__ == '__main__':
    app.secret_key='secret123'
    # app.run(debug=True)
    app.run(debug=True, host='192.168.43.36')
