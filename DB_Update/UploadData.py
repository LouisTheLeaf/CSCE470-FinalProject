import os
from pydoc import classname
import psycopg2
import psycopg2.extras
import csv
import json
import math

def add_professors(cur):
    FillProfessors = "INSERT INTO professors VALUES"
    with open('DB_Update/professors.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            row['Tags']=row['Tags'].replace("'", "")
            FillProfessors+= "("+row['RMP ID']+",'"+row['Last Name']+"','"+row['First Name']+"',"+row['Rating']+","+row['Number of Ratings']+","+row['Retake Percentage']+","+row['Level of Difficulty']+",'"+row['Tags']+"'),"
                    

    FillProfessors=FillProfessors[:-1]+";"
    # print(FillProfessors)
    cur.execute(FillProfessors)


def add_class_data(cur):
    AllFilenames=os.listdir("DB_Update/Classes_Annex")
    Classes =  {}
    for ClassNum in AllFilenames:
        with open('DB_Update/Classes_Annex/'+ClassNum) as f:
            lines=f.readlines()
        linex="".join(lines)
        # print(linex)
        AllClassDict=json.loads(linex)['classes']
        
        Classes[AllClassDict[0]['number']]={}
        # Classes[AllClassDict[0]['number']]['professor']={}
        for sectionNum in AllClassDict:
            # print(sectionNum['prof'])
            if sectionNum['prof'] in Classes[sectionNum['number']].keys():
                Classes[sectionNum['number']][sectionNum['prof']].append(float(sectionNum['gpa']))
            else:
                Classes[sectionNum['number']][sectionNum['prof']]=[]
                Classes[sectionNum['number']][sectionNum['prof']].append(float(sectionNum['gpa']))
        # Classes["110"]
        # print(Classes['110']['WILLIAMS T'])
        f.close()

    #Write to DB
    FillClasses = "INSERT INTO historical VALUES"
    for ClassNum in Classes:
        # print(ClassNum)
        for prof in Classes[ClassNum].keys():
            # print(sum(Classes[ClassNum][prof])/len(Classes[ClassNum][prof]))
            FillClasses+="("+ClassNum+",'"+prof.split(" ")[0]+"',"+str(sum(Classes[ClassNum][prof])/len(Classes[ClassNum][prof]))+"),"
     
    FillClasses=(FillClasses[:-1])
    print(FillClasses)
    # fx = open("DB_Update/demofile2.txt", "a")
    # fx.write(json.dumps(Classes))
    # fx.close
    cur.execute(FillClasses)

    return 0
DATABASE_URL = 'postgres://ojzjasqybnzwna:218f0f774b87ab48cabd578084ec32e5f0358c68d96a236712125929e48aa438@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d50nfdg9435sqf'
# os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
curDict=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
if(conn):
    print('connected!')
    #add_professors(cur)
    add_class_data(cur)
    conn.commit()
# print(os.listdir("DB_Update/Classes_Annex"))


    