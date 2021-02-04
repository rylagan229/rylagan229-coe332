import json
import random

with open('animals.json','r') as f:
    animals = json.load(f)

print(animals['animals'][random.randrange(0,20,1)])
