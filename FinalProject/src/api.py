import json
from flask import Flask, request
import jobs
import requests
import redis
import os
import uuid
import datetime


# Need CRUD routes:
# Create == /Add_Animal
# Read == /Get_Animal/<animal_id>
# Update == /Update_Animal/<animal_id>
# Delete == /deleterange

app = Flask(__name__)

redis_ip = 'rylagan-db'
rd = redis.StrictRedis(host = redis_ip, port=6379, db = 0)

@app.route('/', methods=['GET'])
def instructions():
    return """
    Try these routes:
    /load                        # Populates the redis database with the .json file provided. Can also be used to reset the database
    /Get_Animal                  # Allows the user query an animal id to get the information of the animal
    /Animal_Type/<type>          # Allows the user to sort by the type of Animal 
    /Update_Animal/<animal_id>   # Allows the user to update an animal given the animal's given id
    /Add_Animal                  # Allows the to add an animal
    /deleterange                 # Allows the user to delete animals in a given input date range
    /jobs                        # Gets a list of Jobs
"""

#Route to load the data into the redis database. Can be used to reset data as well
@app.route('/load', methods=['GET'])
def loaddata():
    with open("Latest_Animal_Intakes.json","r") as f:
        intakes = json.load(f)
    
    rd.set('intakes_key', json.dumps(intakes, indent=2))
        
    return 'Database loaded\n'

# Route to fulfill the C of CRUD
@app.route('/Add_Animal', methods = ['GET','POST'])
def Add():
    # Can take either a GET or a POST; will give instructions if GET
    return

# Route to fulfill the R of CRUD
@app.route('/Get_Animal/', methods=['GET'])
def Get_Animal():
    test = get_data()
    output= {}
    animal_id = request.args.get('id')
    for x in test['intakes']:
        if x['id'] == animal_id:
            output = x
    return json.dumps(output)

# Route to fulfill the U of CRUD
@app.route('/Update_Animal/<animal_id>', methods=['GET'])
def Update():
    return

# Route to fulfill the D of CRUD
@app.route('/deleterange', methods=['GET'])
def delete():
    start = request.args.get('start')
    startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    end = request.args.get('end')
    enddate = datetime.datetime.strptime(end,"'%Y-%m-%d_%H:%M:%S.%f'")
    test = get_data()
    
    new_intakes = {}
    new_intakes['intakes'] = []
    
    count = 0
    for i in test['intakes']:
        
        if (datetime.datetime.strptime(test['intakes'][count]['DateTime'], '%Y-%m-%d %H:%M:%S.%f') <= startdate or datetime.datetime.strptime(test['intakes'][count]['DateTime'], '%Y-%m-%d %H:%M:%S.%f')>= enddate):
            new_intakes['intakes'].append(test['intakes'][count])
    
        count = count + 1
   
    rd.set('animals', json.dumps(new_animals, indent=2))

    return json.loads(rd.get('animals')) 

@app.route('/Animal_Type/<Animal_Type>', methods=['GET'])
def SortByType(Animal_Type):
    test = get_data()

    jsonList = test['intakes']

    output = [x for x in jsonList if x['Animal Type'] == Animal_Type]

    return json.dumps(output)

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

def get_data():
    
    return json.loads(rd.get('intakes_key').decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
