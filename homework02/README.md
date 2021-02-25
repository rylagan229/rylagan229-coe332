# README File for COE332 Homework2
Ryan Ylagan rry229

## General Description of the Tools
The following scripts are made to generate 20 animals with random heads and bodies, as well as a random number of arms, legs, and tails. The generate_animals.py file creates these animals and puts them in the form of a dictionary/JSON. The read_animals.py file reads the created JSON file, selects two random animals of the 20 to be parents and creates a child that combines their respective characteristics. This child will have a head and body that combines those of the parents. They will also possess a number of arms, legs, and tails that are the average of the parents' numbers. The script will then print out the parents as well as the child.  

## How to Download and Run the Scripts Directly
In order to run these scripts, run the following into your terminal:
```bash
python3 generate_animals.py animals.json
python3 read_animals.py animals.json
```
## How to Build an Image with the Dockerfile
In order to build an image with the attached dockerfile, run the following commands in your terminal, making sure to replace any instance of 'username' with your Docker Hub username
```bash
docker build -t username/json-parser:1.0 .
```
To ensure that a copy of the image has been built, you can use the command:
```bash
docker images
```
## How to Run the Scripts Inside a Container
To run the scripts inside a container, we will use the docker run command. Remember to replace 'username' with your Docker Hub
```bash
docker run --rm -it username/json-parser:1.0 /bin/bash
```
Once in the container, you can run the following commands:
```bash
cd /home
generate_animals.py test.json
read_animals.py test.json
```
These commands should allow you to be able to run the files and get a proper output.

## How to Run the Unit Test(s) 
To run the Unit Test(s) simply input the following code into your terminal:
```bash
python3 test_read_animals.py
```