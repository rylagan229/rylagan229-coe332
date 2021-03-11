# Description

For this homework, we took our previously created code that randomly generates 20 animals and put it on the Flask App. We also containerized it in flask

## Using the Flask App
In the Flask App you can run the following codes to access specific data:
```
curl localhost:<your portnumber>/animals
curl localhost:<your portnumber>/animals/head/<head_type>
curl localhost:<your portnumber>/animals/legs/<num_legs>
```
Where /animals will return the entire list of animals, /animals/head/<head_type> will return all of the animals on the list with that specific head, and /animals/legs/<num_legs> will return all animals on the list with that number of legs.

## How to build the docker image
Download the dockerfile, app.py, and requirements.txt and input the following code into your terminal
```
docker build -t <name>:latest .
docker run --name "container name" -d -p <your portnumber>:5000 <name>
```
You can then curl the port 
```
curl localhost:<your portnumber>
```

## Running the Consumer File
Simply run the following line of code:
```
python3 animal_consumer.py
```