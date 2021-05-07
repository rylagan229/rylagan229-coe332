# Deployment Manual

## Build the docker image(s)
* Build the required images by going into the Makefile using your preferred editor to change the variables and inputting
```bash
$ make build-all
```

## Start the pods
* cd into the docker directory and run the following commands:
```bash
kubectl apply -f ./api
kubectl apply -f ./db
kubectl apply -f ./wrk
```
* These commands should launch all the needed services and deployments.

* You can check if they are up by inputting the following commands

```bash
$ kubectl get pods
NAME                                               READY   STATUS             RESTARTS   AGE
py-debug-deployment-5cc8cdd65f-dcp9x               1/1     Running            0          21d
rylagan-final-flask-deployment-65dd6457dd-r5s4q    1/1     Running            0          55m
rylagan-final-redis-deployment-5fcf46b69-nxx2q     1/1     Running            0          41m
rylagan-final-worker-deployment-77d7984796-6gft9   1/1     Running            0          13m
```
And
```bash
$ kubectl get services
NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
app1                          NodePort    10.98.88.66     <none>        5000:30154/TCP   29d
rylagan-final-flask-service   ClusterIP   10.99.29.160    <none>        5000/TCP         56m
rylagan-final-redis-service   ClusterIP   10.105.120.63   <none>        6379/TCP         56m
```
and
```bash
$ kubectl get pvc
NAME                 STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
rylagan-final-data   Bound    pvc-84300d43-43b2-43cd-b351-51b726f27778   1Gi        RWO            rbd            103m
```