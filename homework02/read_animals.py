#!/usr/bin/env python3
import json
import random
import sys

def breed(parent1, parent2):
    print('Parent 1:')
    print(parent1)

    print('Parent 2:')
    print(parent2)

    childhead = parent1['head'] + '-' + parent2['head']
    childbody = parent1['body'] + '-' + parent2['body']
    childarms = round((parent1['arms'] + parent2['arms'])/2)
    childlegs = round((parent1['legs'] + parent2['legs'])/2)
    childtails = round((parent1['tail'] + parent2['tail'])/2)

    print('-------------------------------')
    print('Child:')

    child = {
        'head': childhead,
        'body': childbody,
        'arms': childarms,
        'legs': childlegs,
        'tail': childtails
    }

    print(child)
    return child

def main():

    with open(sys.argv[1],'r') as f:
        animal_dict = json.load(f)
        
    parent1 = random.choice(animal_dict['animals'])
    parent2 = random.choice(animal_dict['animals'])
    
    breed(parent1, parent2)

if __name__ == '__main__':
    main()
    
