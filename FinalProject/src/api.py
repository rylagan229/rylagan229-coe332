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

redis_ip = '10.105.227.117'
rd = redis.StrictRedis(host = redis_ip, port=6379, db = 0)

@app.route('/', methods=['GET'])
def instructions():
    return """
    Try these routes:
    /                            # Instructions for different Routes
    /load                        # Populates the redis database with the .json file provided. Can also be used to reset the database if empty or edited
    /Get_All                     # (GET) Returns every intake in the database. There are 3000 entries in the dataset by default
    /Get_Animal/?Animal_ID=...   # (GET) Allows the user query an animal id to get the information of the animal
    /Animal_Type/<type>          # (GET) Allows the user to sort by the type of Animal. Avaliable types are Dog, Cat, Bird, and Other 
    /Update_Animal/?Animal_ID=...# (GET) Allows the user to update an animal given the animal's given id
    /Add_Animal                  # (POST) Allows the user to add an animal by using the json format
    /Delete/?Animal_ID=...       # (GET) Allows the user to delete an animal with a query for their id
    /jobs                        # (GET) Gets a list of Jobs

"""
#@app.route('/run', methods=['GET'])
#def run_jobs():
#
#    return

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
# Adds an animal using a json format
@app.route('/Add_Animal', methods = ['GET','POST'])
def Add():
    try:
        add = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    
    test = get_data()
    test['intakes'].append(add)
    rd.set('intakes_key', json.dumps(test))

    return json.dumps(get_data, indent=2)

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

# Filter by animal type/ extra route (Dog, Cat, Bird, Other)
@app.route('/Animal_Type/<Animal_Type>', methods=['GET'])
def SortByType(Animal_Type):
    test = get_data()
    jsonList = test['intakes']

    output = [x for x in jsonList if x['Animal Type'] == Animal_Type]

    return json.dumps(output, indent=2)

@app.route('/run', methods=['POST'])
def run_job():
    this_uuid = str(uuid4()) 
    this_sequence = str(request.form['seq'])
    data = { 'datetime': str(datetime.now()),
             'status': 'submitted',
             'input': this_sequence }
    rd.hmset(this_uuid, data)
    
    q.put(this_uuid)
    
    return f'Job {this_uuid} submitted to the queue\n'

# Allows the user to submit a Job request
@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end'], job['animal_type']))

# Allows user to see job based on Job ID
@app.route('/jobs/<jobuuid>', methods=['GET'])
def get_job_output(jobuuid):
    byte_dict = rd.hgetall(jobuuid)
    final_dict = {}
    for key, value in bytes_dict.items():
        if key.decode('utf-8') == 'result':
            final_dict[key.decode('utf-8')] = json.loads(value.decode('utf-8'))
        elif key.decode('utf-8') == 'image':
            final_dict[key.decode('utf-8')] = 'ready'
        else:
            final_dict[key.decode('utf-8')] = value.decode('utf-8')
    return json.dumps(final_dict, indent=4)


# Download image based on ID
@app.route('/download/<jobuuid>', methods=['GET'])
def download(jobuuid):
    path = f'/app/{jobuuid}.png'
    with open(path, 'wb') as f:
        f.write(rd.hget(jobuuid, 'image'))
    return send_file(path, mimetype='image/png', as_attachment=True)

def get_data():
    return json.loads(rd.get('intakes_key').decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
