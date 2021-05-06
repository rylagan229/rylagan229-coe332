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
# Read == /Get_Animal
# Update == /Update_Animal/<animal_id>
# Delete == /delete

app = Flask(__name__)

redis_ip = 'rylagan-db'
rd = redis.StrictRedis(host = redis_ip, port=6379, db = 0)

@app.route('/', methods=['GET'])
def instructions():
    return """
    Try these routes:
    /load                        # Populates the redis database with the .json file provided. Can also be used to reset the database
    /Get_All                     # Returns every intake in the database. There are 3000 entries in the dataset by default
    /Get_Animal/?Animal_ID=...   # Allows the user query an animal id to get the information of the animal
    /Animal_Type/<type>          # Allows the user to sort by the type of Animal. Avaliable types are Dog, Cat, and Other 
    /Update_Animal/?Animal_ID=...# Allows the user to update an animal given the animal's given id
    /Add_Animal                  # Allows the to add an animal
    /Delete/?Animal_ID=...       # Allows the user to delete an animal with a query for their id
    /jobs                        # Gets a list of Jobs

"""

#Route to load the data into the redis database. Can be used to reset data as well
@app.route('/load', methods=['GET'])
def loaddata():
    with open("data.json","r") as f:
        intakes_dict = json.load(f)
    
    rd.set('intakes_key', json.dumps(intakes_dict, indent=2))
        
    return 'Database loaded!\n'

@app.route('/Get_All', methods=['GET'])
def GetAll():
    return json.dumps(get_data(), indent=2)

# Route to fulfill the C of CRUD
@app.route('/Add_Animal', methods = ['GET','POST'])
def Add():
    try:
        add = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    
    test = get_data()
    test['intakes'].append(add)
    rd.set('intakes', json.dumps(test))

    return json.dumps(test, indent=2)

# Route to fulfill the R of CRUD
@app.route('/Get_Animal/', methods=['GET'])
def Get_Animal():
    test = get_data()
    output= {}
    animal_id = request.args.get('Animal_ID')
    for x in test['intakes']:
        if x['Animal ID'] == animal_id:
            output = x

    return json.dumps(output, indent = 2)

# Route to fulfill the U of CRUD
@app.route('/Update_Animal/', methods=['GET'])
def Update():
    test = get_data()
    animal_id = request.args.get('Animal_ID')
    name = request.args.get('name')
    intaketype = request.args.get('intaketype')
    intakecondition = request.args.get('intakecondition')
    animaltype = request.args.get('Animal_Type')
    breed = request.args.get('breed')
    color = request.args.get('color')

    intake = {}
    for x in test['intakes']:
        if x['Animal ID'] == animal_id:
            x['Name'] = name
            x['Intake Type'] = intaketype
            x['Intake Condition'] = intakecondition
            x['Animal_Type'] = animaltype
            x['Breed'] = breed
            x['Color'] = color
        
    rd.set('intakes_key', json.dumps(test))
    return json.dumps(intake, indent=2)

# Route to fulfill the D of CRUD
@app.route('/Delete/', methods=['GET'])
def delete():
    test = get_data()
    animal_id = request.args.get('Animal_ID')
    for x in test['intakes']:
        if x['Animal ID'] == animal_id:
            test['intakes'].remove(x)
    
    rd.set('intakes_key', json.dumps(test))

    return 'Animal with ID {} deleted.'.format(animal_id)

@app.route('/Animal_Type/<Animal_Type>', methods=['GET'])
def SortByType(Animal_Type):
    test = get_data()
    jsonList = test['intakes']

    output = [x for x in jsonList if x['Animal Type'] == Animal_Type]

    return json.dumps(output, indent=2)

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
