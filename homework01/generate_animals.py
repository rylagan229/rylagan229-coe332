import json
import petname
import random

data = {}
data['animals'] = []
head = ['snake', 'bull', 'lion', 'raven', 'bunny']

for i in range(20):
    arms = random.randrange(2,11,1)
    legs = random.randrange(3,13,1)
    tail = arms + legs
    body1 = petname.name()
    body2 = petname.name()
    
    while (body1 == body2):
        body2 = petname.name()

    body = body1 + "-" + body2

    data['animals'].append({'head': head[random.randrange(0,5,1)], 'body': body, 'arms': arms, 'legs': legs, 'tail' : tail})

with open('animals.json','w') as out:
    json.dump(data, out, indent=2)
