# User Manual/Description
User guide on how to operate/interact with the app

## Overview
The point of the app is to use data taken from a data set and allow the user to use CRUD operations (Create, Read, Update, and Delete). The data I have chosen to use is one that documented the latest 3000 intakes at the Austin Animal Center.

## The data
The original data set can be found at the link [here](https://data.world/rebeccaclay/austin-tx-animal-center-stats/workspace/file?filename=Austin_Animal_Center_Intakes.csv). It originally includes data that goes as far back as 2013 up until 05/05/2021. It contains a total of 125,844 entries that are that are each identified by their Animal ID, Name, DateTime, MonthYear, Found Location, Intake Type, Intake Condition, Animal Type, Sex upon Intake, Age upon Intake, Breed, and their Color. To make the data more concise for this project, I cut down the entries to the latest 3000 intakes, and as such the available dates range from 12/16/2020 to 5/5/2021. The cut down data can be found in the provided ```data.json``` file.

## How to Run and Operate the API Once Deployed:    
Assuming everything has properly been deployed, you can then Exec into a python debug container:
```
$ kubectl exec -it py-debug-deployment-5cc8cdd65f-dcp9x -- /bin/bash
```
From there, you may start curling routes to get apply the CRUD operations on the database.

### Routes
#### /
* Simply returns instructions on what routes are available, which are shown below
```
$ curl 10.99.29.160:5000/ 
 Try these routes:
    /                            # Instructions for different Routes
    /load                        # Populates the redis database with the .json file provided. Can also be used to reset the database if empty or edited
    /Get_All                     # (GET) Returns every intake in the database. There are 3000 entries in the dataset by default
    /Get_Animal/?Animal_ID=...   # (GET) Allows the user query an animal id to get the information of the animal
    /Animal_Type/<type>          # (GET) Allows the user to sort by the type of Animal. Avaliable types are Dog, Cat, Bird, and Other
    /Update_Animal/?Animal_ID=...# (GET) Allows the user to update an animal given the animal's given id
    /Add_Animal                  # (POST) Allows the user to add an animal by using the json format
    /Delete/?Animal_ID=...       # (GET) Allows the user to delete an animal with a query for their id
    /jobs                        # (GET) Gets a list of Jobs
    /download/<jobuuid>
```
#### /load
* You need to load the database first in order to use the data, otherwise this route can be used to reset the database after altering it
```
$ curl 10.99.29.160:5000/load
Database loaded!/n
```

#### /Get_All
* Allows the User to return the entire Data set.
```
$ curl 10.99.29.160:5000/Get_All
{
   "intakes":[
      {
         "Animal ID":"A833800",
         "Name":"",
         "DateTime":"5/5/2021 17:08",
         "MonthYear":"5/5/2021 17:08",
         "Found Location":"2321 Kale Drive in Austin (TX)",
         "Intake Type":"Stray",
         "Intake Condition":"Normal",
         "Animal Type":"Cat",
         "Sex upon Intake":"Unknown",
         "Age upon Intake":"2 months",
         "Breed":"Domestic Shorthair",
         "Color":"Chocolate/Seal Point"
      },
.
.
.
.
```
#### /Add_Animal
* Allows the user to post a json to add an animal to the database
```
curl -X POST -H "content-type: application/json" -d '{ "Animal ID":"A123456", "Name":"", "DateTime":"5/5/2021 17:08", "MonthYear":"5/5/2021 17:08", "Found Location":"2321 Kale Drive in Austin (TX)", "Intake Type":"Stray","Intake Condition":"Normal", "Animal Type":"Cat", "Sex upon Intake":"Unknown", "Age upon Intake":"2 months", "Breed":"Domestic Shorthair","Color":"Chocolate/Seal Point" }}'   10.105.227.117:5000/Add_Animal
```

#### /Get_Animal/?Animal_ID=...
* Queries for and Animal ID then gets the data for that specific animal
```
$ curl 10.99.29.160:5000/Get_Animal/?Animal_ID=A806287
 {
         "Animal ID":"A806287",
         "Name":"Roulette",
         "DateTime":"5/5/2021 16:51",
         "MonthYear":"5/5/2021 16:51",
         "Found Location":"Austin (TX)",
         "Intake Type":"Owner Surrender",
         "Intake Condition":"Normal",
         "Animal Type":"Dog",
         "Sex upon Intake":"Spayed Female",
         "Age upon Intake":"5 years",
         "Breed":"Pit Bull Mix",
         "Color":"Brown"
 },
```

#### /Update_Animal/?Animal_ID=...
* Allows the User to update an Animal's information given their Animal Id
```
$ curl 10.99.29.160:5000/Update_Animal/?Animal_ID=A806287&name=Ryan&intaketype=Stray&intakecondition=Normal&animaltype=Cat&breed=Tabby&Color=Black
{
         "Animal ID":"A806287",
         "Name":"Ryan",
         "DateTime":"5/5/2021 16:51",
         "MonthYear":"5/5/2021 16:51",
         "Found Location":"Austin (TX)",
         "Intake Type":"Stray",
         "Intake Condition":"Normal",
         "Animal Type":"Cat",                                                                                                                                                                                                                        "Sex upon Intake":"Spayed Female",
         "Age upon Intake":"5 years",
         "Breed":"Tabby",
         "Color":"Black"
 },
```

#### /Delete
* Allows the user to delete an Animal given their Animal ID```
$ curl 10.99.29.160:5000/Get_Animal/?Animal_ID=A806287
Animal with ID A806287 deleted.
```
#### /Animal_Type/<Animal_Type>
* Returns all animals with the input type. Available types are Dog, Cat, Bird, and Other.
```
$ curl 10.99.29.160:5000/Animal_Type/Dog
},
      {
         "Animal ID":"A806287",
         "Name":"Roulette",
         "DateTime":"5/5/2021 16:51",
         "MonthYear":"5/5/2021 16:51",
         "Found Location":"Austin (TX)",
         "Intake Type":"Owner Surrender",
         "Intake Condition":"Normal",
         "Animal Type":"Dog",
         "Sex upon Intake":"Spayed Female",
         "Age upon Intake":"5 years",
         "Breed":"Pit Bull Mix",
         "Color":"Brown"
      },
      {
         "Animal ID":"A824509",
         "Name":"Koda",
         "DateTime":"5/5/2021 16:32",
         "MonthYear":"5/5/2021 16:32",
         "Found Location":"12220 Hunters Chase Drive in Austin (TX)",
         "Intake Type":"Stray",
         "Intake Condition":"Normal",
         "Animal Type":"Dog",
         "Sex upon Intake":"Neutered Male",
         "Age upon Intake":"2 years",
         "Breed":"Akita",
         "Color":"Brown/White"
      },
.
.
.
.
```
### Job Routes
#### /job
* Allows the user to submit a job request that graph the Amount of Intakes between the two entered dates
```
$ curl -X POST -d  10.99.29.160:5000
```

#### /download/<jobuuid>
* Downloads the image created by the job with the jobuuid that was input
```
curl 10.99.29.160:5000/download/<jobuuid>
```