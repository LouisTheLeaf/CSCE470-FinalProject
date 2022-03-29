from flask import Flask, render_template,request
from SearchFunctions import *

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def getInfo():
    data = searchDB()
    return render_template('frontproto.html', data=data)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.form['name']
    return render_template('frontproto.html', name=name)
