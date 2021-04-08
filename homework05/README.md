# Homework 5 COE332

We modify our hello pod given to us during lecture to print a name and a deployment to print our name, as well as the pod's IP

## Part A
Create the pod using the hellomodified_A.yml file and running the command:
```bash
kubectl apply -f hellomodified_A.yml
```
You can then get the logs of the pod by inputting:
```bash
kublectl logs pod/hello
```
Which outputs the following:
```
Hello,
```
Which is not the desired output. This is because we did not include a name for the environment variable

To delete the pod, run the following:
```bash
kubectl delete pods hello
```

## Part B
Create the pod using the hellomodified_B.yml file and running the command:
```bash
kubectl apply -f hellomodified_B.yml

```
You can then get the logs of the pod by inputting:
```bash
kublectl logs pod/hello
```
Which outputs the following:
```
Hello, Ryan
```
Which is our desired output.

To delete the pod, run the following:
```bash
kubectl delete pods hello
```
## Part C
Create the deployment using the hellomodified_C.yml file and running the command:
```bash
kubectl apply -f hellomodified_C.yml

```
You can get the list of the pods and their respective IP addresses by running the following:
```bash
kubectl get pods -o wide
```
Doing so should display something like:
```bash
NAME                                READY   STATUS    RESTARTS   AGE   IP             NODE   NOMINATED NODE   READINESS GATES
hello-deployment-78d4f4956c-b2lfs   1/1     Running   0          20m   10.244.3.195   c01    <none>           <none>
hello-deployment-78d4f4956c-f8n86   1/1     Running   0          20m   10.244.5.135   c04    <none>           <none>
hello-deployment-78d4f4956c-kj5lz   1/1     Running   0          20m   10.244.7.148   c05    <none>           <none>
```

You can then get the pods' logs by running the following code, displayed alongside their respective outputs:
```bash
kubectl logs hello-deployment-78d4f4956c-b2lfs

Hello, Ryan from IP 10.244.3.195
```
```bash
kubectl logs hello-deployment-78d4f4956c-f8n86

Hello, Ryan from IP 10.244.3.135
```
```bash
kubectl logs hello-deployment-78d4f4956c-kj5lz

Hello, Ryan from IP 10.244.3.148
```