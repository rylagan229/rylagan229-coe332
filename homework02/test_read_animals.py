#!/usr/bin/env python3
import unittest
import sys
from read_animals import breed

class TestReadAnimals(unittest.TestCase):
    
    def test_breed(self):
        parent1 = {
            'head': 'bunny',
            'body': 'falcon-boxer',
            'arms': 6,
            'legs': 12,
            'tail': 18
        }

        parent2 = {
            'head': 'raven',
            'body': 'fawn-goblin',
            'arms': 4,
            'legs': 3,
            'tail': 7
        }
        self.assertEqual(breed(parent1, parent2), {'head': 'bunny-raven', 'body': 'falcon-boxer-fawn-goblin', 'arms': 5, 'legs':  8, 'tail': 12})
        self.assertRaises(TypeError, breed,'string1','string2')

if __name__ == '__main__':
    unittest.main()
