import json
from flask import Flask, request
import jobs
import requests
import redis
import os
import uuid
import datetime

app = Flask(__name__)

rd = redis.StrictRedis(host='10.105.227.117', port=6379, db = 0)

@app.route('/helloworld', methods=['GET'])
def helloworld():
#simple hello world route just for testing
    return "hello world!"

@app.route('/', methods=['GET'])
def instructions():
    return """
    Try these routes:
    /loaddata
    /sortbystate/<stateID>
    /getcity
    /jobs
"""
#Route to load the data into the redis database. Can be used to reset data as well
@app.route('/load', methods['GET'])
def loaddata():
    with open("US_City_Pop_Above_50000.json","r") as f:
        citydata = json.load(f)
    count = 0
    for city in citydata:
        table_id = city['Table_Id']
        CityName = city['City']
        Summary_Level = city['Summary_Level']
        Geo_Id = city['Geo_Id']
        State = city['State']
        State_Fips = city['State_Fips']
        Total_Pop = city['Total_Population']
        
        count = count + 1
        rd.set('city', json.dumps(city, indent=2))
        
    return json.loads(rd.get('city'))

@app.route('/sortbystate/<stateID>', methods=['GET'])
def sortbystate(stateID):

    return

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
