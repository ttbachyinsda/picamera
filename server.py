from flask import Flask, request, g, session, redirect, url_for
from flask import render_template, render_template_string, send_file, send_from_directory
from pidetect import generatemarkdown
import os

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/report')
def report():
    filename = generatemarkdown()
    return filename

@app.route('/getzip/<filename>')
def getzip(filename):
    directory = os.getcwd()
    return send_from_directory(directory, filename+'.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
