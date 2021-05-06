# Deployment Manual

## Start the pods
* cd into the docker directory and run the following commands:
```bash
kubectl apply -f ./api
kubectl apply -f ./db
kubectl apply -f ./wrk
```