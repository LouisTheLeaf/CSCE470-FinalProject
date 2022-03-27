import os
import psycopg2
import psycopg2.extras


DATABASE_URL = 'postgres://ojzjasqybnzwna:218f0f774b87ab48cabd578084ec32e5f0358c68d96a236712125929e48aa438@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d50nfdg9435sqf'
# os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
curDict=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
if(conn):
    print('connected!')
    curDict.execute("SELECT * FROM testtable;")
    print(curDict.fetchall())
    
    


