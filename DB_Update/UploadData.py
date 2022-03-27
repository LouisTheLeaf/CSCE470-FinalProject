import os
import psycopg2
import psycopg2.extras
import csv

DATABASE_URL = 'postgres://ojzjasqybnzwna:218f0f774b87ab48cabd578084ec32e5f0358c68d96a236712125929e48aa438@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d50nfdg9435sqf'
# os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
curDict=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
if(conn):
    print('connected!')
    # curDict.execute("SELECT * FROM testtable;")
    # print(curDict.fetchall())


with open('professors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
    print(f'Processed {line_count} lines.')
    