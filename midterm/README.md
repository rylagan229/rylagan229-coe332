# Description

For this homework, we took our previously created code that randomly generates 20 animals and put it on the Flask App and created a database of the animals using redis. We also containerized it in flask and redis and connected the two using a docker-compose. We added many new routes that utilize queries.

## Using the Flask App
In the Flask App you can run the following codes to access specific data:
```
curl localhost:<your portnumber>/animals
curl localhost:<your portnumber>/animals/<uuid>
curl localhost:<your portnumber>/animals/legsaverage
curl localhost:<your portnumber>/animals/count
```
Where /animals will return the entire list of animals, /animals/<uuid> passes a uuid and returns the respective animal with the identifier, /animals/legsaverage returns the average number of legs among the animals, and /animals/count returns the total number of animals.  

We also have three more routes, these ones however require the use of queries to operate properly. Both the /daterange and /deleterange require a start and end time in the form of Year-month-day_Hour:Minute:Seconds. The /edit requires the query for the specfic uuid and the respective value and strings wanted to 'update' the chosen animal. 

```
curl localhost:<your portnumber>/animals/daterange
curl localhost:<your portnumber>/animals/edit
curl localhost:<your portnumber>/animals/deleterange
```

## How to connect the Flask container and the redis container
Download the contents of the redis-docker subfolder. Make sure neither your redis port or your flask port are listening or occupied. Run the following code.
```
docker-compose -p <name> up
```
This command will containerize both flask and redis and allows functionality at the use of one command. 