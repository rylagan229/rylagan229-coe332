import json
import redis
import datetime
from flask import Flask, request, jsonify
import datetime
import petname
import uuid
import random
import os

app = Flask(__name__)

RD_HOST = os.environ.get('RD_HOST')
rd = redis.StrictRedis(host= RD_HOST, port= 6379, db=0)

@app.route('/animals', methods=['GET'])
def get_animals():
    data = get_data()
    jsonList = data['animals']
    return jsonify(jsonList)

@app.route('/animals/daterange', methods=['GET'])
def querydate():

    start = request.args.get('start')
    startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    end = request.args.get('end')
    enddate = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
    test = get_data()

    return json.dumps([x for x in test['animals'] if (datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f') >= startdate and datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f')<= enddate ) ])

@app.route('/animals/<uuid>', methods=['GET'])
def uuid_select(uuid):
    test = get_data()

    jsonList = test['animals']
    
    output = [x for x in jsonList if x['uuid'] == uuid]

    return json.dumps(output)

@app.route('/animals/edit', methods=['GET'])
def edit_animal():
    test = get_data()
    rd = redis.StrictRedis(host= RD_HOST, port=6379, db=0)
    uuid = request.args.get('uuid')
    head = request.args.get('head')
    arms = request.args.get('arms')
    body = request.args.get('body')
    tail = request.args.get('tail')
    legs = request.args.get('legs')

    i = [i for (i,x) in enumerate(test['animals']) if x['uuid'] == uuid]

    test['animals'][i[0]]['head'] = str(head)
    test['animals'][i[0]]['body'] = str(body)
    test['animals'][i[0]]['arms'] = int(arms)
    test['animals'][i[0]]['tail'] = int(tail)
    test['animals'][i[0]]['legs'] = int(legs)
    
    rd.set('animals', json.dumps(test, indent=2))
    
    return json.loads(rd.get('animals'))

@app.route('/animals/deleterange', methods=['GET'])
def delete():
    start = request.args.get('start')
    startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
    end = request.args.get('end')
    enddate = datetime.datetime.strptime(end,"'%Y-%m-%d_%H:%M:%S.%f'")
    test = get_data()
    new_animals = {}
    new_animals['animals'] = []

    count = 0
    for i in test['animals']:
        
        if (datetime.datetime.strptime(test['animals'][count]['created_on'], '%Y-%m-%d %H:%M:%S.%f') <= startdate or datetime.datetime.strptime(test['animals'][count]['created_on'], '%Y-%m-%d %H:%M:%S.%f')>= enddate):
            new_animals['animals'].append(test['animals'][count])
    
        count = count + 1
   
    rd.set('animals', json.dumps(new_animals, indent=2))

    return json.loads(rd.get('animals')) 

@app.route('/animals/legaverage', methods=['GET'])
def leg_average():
    test = get_data()
    jsonList = test['animals']
    total = 0.0
    count = 0

    for i in jsonList:
        total = float(i['legs']) + total
        count = count + 1
    
    average = float(total/count)

    return str(average)

@app.route('/animals/count', methods=['GET'])
def count():
    test = get_data()
    count = 0
    jsonList = test['animals']

    for i in jsonList:
        count = count + 1

    return str(count)

@app.route('/loaddata', methods=['GET'])
def load():
    animal_dict = {}
    animal_dict['animals'] = []
    head = ['snake', 'bull', 'lion', 'raven', 'bunny']

    for i in range(20):
        arms = random.randrange(2,11,2)
        legs = random.randrange(3,13,3)
        tail = arms + legs
        body1 = petname.name()
        body2 = petname.name()
    
        while (body1 == body2):
            body2 = petname.name()

        body = body1 + "-" + body2

        created_on = str(datetime.datetime.now())
        uid = str(uuid.uuid4())

        animal_dict['animals'].append({'head': head[random.randrange(0,5,1)], 'body': body, 'arms': arms, 'legs': legs, 'tail' : tail, 'created_on': created_on,'uuid': uid})

    rd = redis.StrictRedis(host= RD_HOST, port=6379, db=0)
    rd.set('animals', json.dumps(animal_dict, indent=2))

    return jsonify(animal_dict)


def get_data():
    rd = redis.StrictRedis(host= RD_HOST, port = 6379, db = 0)
    data = json.loads(rd.get('animals'))
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
