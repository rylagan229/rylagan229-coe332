#!/usr/bin/env python3
import json
import petname
import random
import sys
import datetime
import uuid
import redis

def main():
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

    rd = redis.StrictRedis(host='127.0.0.1', port=6420, db=0)
    rd.set('animals', json.dumps(animal_dict, indent=2))
    print(json.loads(rd.get('animals')))

if __name__ == '__main__':
    main()
