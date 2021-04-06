# Description

For this homework, we took our previously created code that randomly generates 20 animals and put it on the Flask App and created a database of the animals using redis. We also containerized it in flask and redis and connected the two using a docker-compose. We added many new routes that utilize queries.

## Containerizing the Flask App/Redis
Navigate to the downloaded repository and input the following code to create and run the container:
```
docker-compose up -d
```

In order to populate the redis database, use the following route to add animals.
Failing to do so will result in the routes returning nothing due to the database being empty.
```
curl localhost:5040/loaddata
```

## Using the Flask App
In the Flask App you can run the following codes to access specific data:
```
curl localhost:5040/animals
curl localhost:5040/animals/<uuid>
curl localhost:5040/animals/legsaverage
curl localhost:5040/animals/count
```
Where /animals will return the entire list of animals, /animals/<uuid> passes a uuid and returns the respective animal with the identifier, /animals/legsaverage returns the average number of legs among the animals, and /animals/count returns the total number of animals.  

We also have three more routes, these ones however require the use of queries to operate properly. Both the /daterange and /deleterange require a start and end time in the form of Year-month-day_Hour:Minute:Seconds. The /edit requires the query for the specfic uuid and the respective value and strings wanted to 'update' the chosen animal. Below are the routes that utilize queries with an example of their input.

```
curl "localhost:5040/animals/daterange?start='2021-04-05_20:01:20.450681'&end='2021-04-05_20:01:20.460093'"
curl "localhost:5040/animals/edit/?uuid=4b854246-c56b-4d65-a330-32e5a955ad87&head=duck&arms=10&body=molly-jaguar&tail=6&legs=12"
curl "localhost:5040/animals/deleterange?start='2021-04-05_20:01.20.450681'&end='2021-04-05_20:01:20.460093'"
```
## Closing the containers
After you are done using the containers, you have to close them by using the command
```
docker-compose down
```