# Repository for the Module Digital Technologies in the Master Course Digital Transformation

This repo contains code for the module digital tech in the masters course digital transformation.


## Webapi Examples
I have provided three examples to demonstrate simple webapi deployments. You can check it out by following the below instructions. The provided shell scripts make it as easy as possible to run them. However, please also review the files and check out the documentations of docker, docker-compose, and kubernetes to understand the mechanics.

### Webapi Flask
The folder `webapi_flask`contains Python code to start a simple server that simply returns "Hello World!".
To run it, you have two options:
1. install all dependencies via `pip install -r requirements.txt` (recommended to create a virtual environment first via `python -m venv venv` and subsequently `source venv/bin/activate`) and then run `python src/start_server.py` --> you can then access the browser at `localhost:8080` to see the result
2. build an image with docker. The command is stored in `build_image.sh`, which you can run. To run the server subsequently run `run_container.sh` --> you can then access the browser at `localhost:80`; to stop the container, run the command `stop_container.sh`

### Webapi via Docker Compose
The folder `webapi_docker_compose` contains a little more sophisticated app with a backend, which is a redis (in memory) database. 
- To start it, run the script `start_deployment.sh`, which builds the image from the source code and starts both backend and frontend --> you can access it via `localhost:80`
- To stop it, run the script `stop_deployment.sh`

### Webapi via Kubernetes
The folder `webapi_k8s` contains the same app as the one for docker compose, but ready to be run in k8s. For that, you need to install k8s first (either docker desktop or minicube). 
- To start it, run the script `start_deployment.sh`, which builds the image from the source code and starts both backend and frontend 
- Once started, run the command `kubectl get service` and checkthe details of the service. It will say something like `web          NodePort    10.110.9.12     <none>        80:31784/TCP   11s`, which tells you that you can access it via `localhost:31784` (the port mapped to 80)
- To stop it, run the script `stop_deployment.sh`
