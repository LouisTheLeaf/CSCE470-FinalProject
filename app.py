from flask import Flask, render_template,request
from SearchFunctions import *
import os
from pydoc import classname
import psycopg2
import psycopg2.extras
import csv
import json
import math

app = Flask(__name__, template_folder='templates')
name = ""

def getData():
    data = cheese
    return data#searchDB(name)

@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('frontproto.html', data=data)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.form['name']
    return render_template('frontproto.html', name=name)
