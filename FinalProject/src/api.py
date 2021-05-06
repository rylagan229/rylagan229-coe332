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
    /load                        # Populates the redis database with the .json file provided
    /Get_Animal/<animal_id>      # Allows the user to get the entire information of an animal given their animal id
    /Animal_Type/<type>          # Allows the user to sort by the type of Animal 
    /Update_Animal/<animal_id>   # Allows the user to update an animal given the animal's given id
    /Add_Animal                  # Allows the to add an animal
    /deleterange                 # Allows the user to delete animals in a given input date range
    /jobs                        #
"""

#Route to load the data into the redis database. Can be used to reset data as well
@app.route('/load', methods['GET'])
def loaddata():
    with open("Latest_Animal_Intakes.json","r") as f:
        intakes = json.load(f)
    count = 0
    for animal in intakes:
        Animal_Id = intakes['Animal_Id']
        Name = intakes['Name']
        DateTime = intakes['DateTime']
        MonthYear = intakes['MonthYear']
        Location_Found = intakes['Found Location']
        Intake_Type = intakes['Intake Type']
        Intake_Condition = intakes['Intake_Condition']
        Animal_Type = intakes['Animal Type']
        Sex_upon_Intake = intakes['Sex upon Intake']
        Age_upon_Intake = intakes['Age upon Intake']
        Breed = intakes['Breed']
        Color = intakes['Color']
        
        count = count + 1
        rd.set('intakes', json.dumps(intakes, indent=2))
        
    return json.loads(rd.get('intakes'))

@app.route('/Animal_Type/<Animal_Type>', methods=['GET'])
def SortByType(Animal_Type):
    test = get_data()

    jsonList = test['intakes']

    output = [x for x in jsonList if x['Animal Type'] == Animal_Type]

    return json.dumps(output)

@app.route('/get_Animal/<animal_id>', methods=['GET'])
def getcity(animal_id):
    test = get_data()

    jsonList = test['animals']
    
    output = [x for x in jsonList if x['Animal Id'] == animal_id]

    return json.dumps(output)

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

def get_data():
    rd = redis.StrictRedis(host=redis_ip, port=6379, db = 0)
    data = json.loads(rd.get('intakes'))
    
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
