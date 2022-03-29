import os
from pydoc import classname
import psycopg2
import psycopg2.extras
import csv
import json
import math

# DATABASE_URL = 'postgres://ojzjasqybnzwna:218f0f774b87ab48cabd578084ec32e5f0358c68d96a236712125929e48aa438@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d50nfdg9435sqf'
# # os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL)
# cur = conn.cursor()
# curDict=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# if(conn):

# HOW TO USE
# SEARCHDB() IS ALL YOU NEED AND WILL RETURN AN A NESTED LIST WITH
# INDEX 0 WITH HISTORICAL DATA AND INDEX 1 has RMP data
# index 0: Historical data (course number, prof last name, avg GPA)
# index 1: RMP data (rmp_id  |    last_name    |  first_name  | rating | num_ratings | retake_percent | difficulty |)
def searchRMP(query,curDict):
    RMP_Prof={}
    SQL ="Select * FROM professors WHERE last_name LIKE (%s)"
    data = (query,)
    curDict.execute(SQL,data)
    RMP_Prof=(curDict.fetchall())
    if bool(RMP_Prof): #checks if not empty if empty then gives empty []
        RMP_Prof=RMP_Prof[0]
    # print(RMP_Prof)
    return RMP_Prof
def searchDB(query):
    DATABASE_URL = 'postgres://ojzjasqybnzwna:218f0f774b87ab48cabd578084ec32e5f0358c68d96a236712125929e48aa438@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d50nfdg9435sqf'
    conn = psycopg2.connect(DATABASE_URL)
    curDict=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    DBData=[]

    SQL ="Select * FROM historical WHERE classnum=(%s);"
    data = (query,)
    curDict.execute(SQL,data)

    AllProf=curDict.fetchall()
    #print(AllProf)
    RMP=[]
    for prof in AllProf:
        RMP.append(searchRMP(prof[1],curDict))
    DBData=[AllProf,RMP]
    #print(RMP)
    return DBData
def main():
    DATABASE_URL = 'postgres://ojzjasqybnzwna:218f0f774b87ab48cabd578084ec32e5f0358c68d96a236712125929e48aa438@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d50nfdg9435sqf'
    # os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    curDict=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = "Leyk"
    q2 = '110'
    if(conn):
        # searchRMP(query,curDict)
        AllProfessorData=searchDB(q2)
<<<<<<< HEAD
        print(AllProfessorData[0][0],AllProfessorData[1][0])
# main()
=======
        #print(AllProfessorData[0][0],AllProfessorData[1][0])
main()
>>>>>>> ed23978a279826dd360a9aad2c26fba61725d93e
