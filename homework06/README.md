# Homework06
## Creating the Services
First, you need to create the respective services. Do so using the following input:
```bash
kubectl apply -f rylagan-test-flask-service.yml

kubectl apply -f rylagan-test-redis-service.yml
```
You need to then change the host ip. You can do so by inputting the command:
```bash
kubectl get services
```
Which should output something like the following:
```bash
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
rylagan-test-flask-service   ClusterIP   10.103.238.197   <none>        5000/TCP         3h40m
rylagan-test-redis-service   ClusterIP   10.109.76.73     <none>        6379/TCP         3h40m
```
Using the ips given, got into the rylagan-test-flask-deployment.yml file and change the value of RD_HOST to the redis cluster-ip in your preferred editor. In this case, it would be 10.109.76.73.

You're then ready to start the deployments with the following:
```bash
kubectl apply -f rylagan-test-flask-deployment.yml

kubectl apply-f rylagan-test-redis-deployment.yml

kubectl apply -f pythondebug.yml

kubectl apply -f rylagan-test-redis-pvc.yml
```

You can then check the running pods using
```bash
kubectl get pods
```
## Python Debug Shell
You can know exec into the python debug container using:
```bash
kubectl exec -it <container name> -- /bin/bash
```
Once in, you need to install redis and curl, after which you are ready to use the commands and routes outlined in the midterm's README.md file.