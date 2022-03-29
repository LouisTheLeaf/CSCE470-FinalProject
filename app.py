from flask import Flask, render_template, request
from SearchFunctions import *
import psycopg2
import psycopg2.extras
app = Flask(__name__, template_folder='templates')

def getData():
    print("ran getData()")
    if request.method == "POST":
        query_from_form = request.form['query']
        print("getData query: "+query_from_form)
        dbResults = searchDB( str(query_from_form) )
    return dbResults

#@app.route('/results', methods=['GET', 'POST'])
#def results():
#    return render_template('frontproto.html', data=data)

@app.route('/', methods=['GET', 'POST'])
def index():
    profs = []
    rmp = []
    dbResults = [profs,rmp]
    if request.method == "POST":
        query_from_form = request.form['query']
        print("getData query: "+query_from_form)
        if query_from_form:
            dbResults = searchDB( str(query_from_form) )
    return render_template('frontproto.html', data=dbResults)
