from flask import Flask, render_template, request
from SearchFunctions import *
import psycopg2
import psycopg2.extras
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    profs = []
    rmp = []
    dbResults = [profs,rmp]
    user_searched = 0
    if request.method == "POST":
        user_searched = 1
        query_from_form = request.form['query']
        print("getData query: "+query_from_form)
        if query_from_form.isdigit():
            print("the query is not a string")
            dbResults = searchDB( str(query_from_form) )
    return render_template('frontproto.html', data=dbResults, search=user_searched)

if __name__ == '__main__':
    my_awesome_app.run()
