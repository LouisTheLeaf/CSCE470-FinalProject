from flask import Flask, render_template,request
from SearchFunctions import *
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('frontproto.html')


