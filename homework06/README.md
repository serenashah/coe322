# Kubernetes Deployment for Meteorite Landings Database Server
This project uses Kubernetes (k8s) to deploy a test environment that is suitable to interact with a Flask web application using a Redis database which allows users to load and receive datasets containing information about specific meteors sighted and is provided by the Meteorical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g). The scripts included in this project are:
- ```Dockerfile```: Downloads necessary dependencies and environment variables for the Flask application.
- ```app.py```: Provides routes to download and return the Meteorite Landings data set.
There are additionally five yaml files which when used on a Kubernetes cluster create the environment necessary to interact with the API:
- ```s-shah-test-redis-deployment.yml```: Creates a deployment for the Redis database
- ```s-shah-test-redis-pvc.yml```: Stores the data written to it from the deployment file independently from the pods
- ```s-shah-test-redis-service.yml```: Provides a persistent IP address to use that is able to interact with Redis
- ```s-shah-test-flask-deployment.yml```: Creates a deployment (with two replicas) for the Flask API
- ```s-shah-test-flask-service.yml```: Provides a persistent IP address to use that is able to interact with the API
