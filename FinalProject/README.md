# COE332 Final Project
Ryan Ylagan rry229

## Introduction
* Uses data that contains the latest intakes from the Austin Animal Center.
* The full original, undedited dataset can be found [here](https://data.world/rebeccaclay/austin-tx-animal-center-stats/workspace/file?filename=Austin_Animal_Center_Intakes.csv) 
* The data availabes ranges from 12/16/2020 to 5/5/2021 and contains the latest 3000 intakes.

* The ultimate goal of this API is to have three containerized components, of which are listed below:
1. A front end for submitting jobs
2. A containerized redis database to store data and jobs
3. A back end worker that runs an analysis job