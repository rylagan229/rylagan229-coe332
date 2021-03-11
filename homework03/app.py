import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/animals', methods=['GET'])
def get_animals():
    return json.dumps(get_data())

@app.route('/animals/head/<head_type>', methods=['GET'])
def get_animal_heads(head_type):
   test = get_data()
   print(type(test))

   jsonList = test['animals']

   output = [x for x in jsonList if x['head'] == head_type]
   print(output)
   
   return json.dumps(output)

@app.route('/animals/legs/<num_legs>', methods=['GET'])
def get_animal_legs(num_legs):
    test = get_data()
    print(type(test))

    jsonList = test['animals']
          
    output = [x for x in jsonList if x['legs'] == int(num_legs)]
    print(output)

    return json.dumps(output)

def get_data():
    with open("animals.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
