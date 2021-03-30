import json
import redis
import datetime
from flask import Flask, request

app = Flask(__name__)
rd = redis.StrictRedis(host='127.0.0.1', port=6420,db=0)

@app.route('/animals', methods=['GET'])
def get_animals():
    return json.loads(rd.get('animals'))

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
    total_new = 0
    count = 0

    for i in jsonList:
        total_old = jsonList[count]['legs']
        total_new = total_new + total_old 
        count = count + 1
    
    average = (total_new/count)

    return str(average)

@app.route('/animals/count', methods=['GET'])
def count():
    test = get_data()
    count = 0
    jsonList = test['animals']

    for i in jsonList:
        count = count + 1

    return str(count)

def get_data():

    return json.loads(rd.get('animals'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
