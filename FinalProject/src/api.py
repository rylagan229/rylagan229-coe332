import json
from flask import Flask, request
import jobs
import requests
import redis

app = Flask(__name__)

rd = redis.StrictRedis(host='10.105.227.117', port=6379, db = 0)

@app.route('/helloworld', methods=['GET'])
def helloworld():
    return "hello world"

@app.route('/', methods=['GET'])
def instructions():
    return """
    Try these routes:

"""
@app.route('/load', methods['GET'])
def load():
    loaddata()
    return json.dumps(get_data())

def load_data():
    return 

def get_data():
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
