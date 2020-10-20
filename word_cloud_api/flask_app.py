
from flask import Flask
from flask import send_file
from src.abr import main as abr_main

import os
from flask import flash, request, redirect


app = Flask(__name__)
app.debug = True
ALLOWED_EXTENSIONS = {'txt'}


@app.route('/')
def hello_world():
    return 'Hello, welcome to this service!\n use http://rsharifnasab.pythonanywhere.com/text'


@app.route('/text2')
def create_from_text():
	    print("salam")
	    abr_main("this is sample word cloud")
	    return send_file('out/text.png', mimetype='image/png')



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/text', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash('not supported format')
            return redirect(request.url)

        if file:
            text = file.read().decode("utf-8")
            abr_main(text)
            return send_file('out/text.png', mimetype='image/png')


    return '''
    <!doctype html>
    <title>Upload txt File</title>
    <h1>Upload a txt file to create word cloud</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
