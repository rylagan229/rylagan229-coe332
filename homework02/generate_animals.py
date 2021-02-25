#!/usr/bin/env python3
import json
import petname
import random
import sys

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

        animal_dict['animals'].append({'head': head[random.randrange(0,5,1)], 'body': body, 'arms': arms, 'legs': legs, 'tail' : tail})

    with open(sys.argv[1],'w') as f:
        json.dump(animal_dict, f, indent=2)

if __name__ == '__main__':
    main()
