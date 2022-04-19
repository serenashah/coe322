# Kubernetes Deployment for Meteorite Landings Database Server
This project uses Kubernetes to deploy a test environment that is suitable to interact with a Flask web application which allows users to load and receive datasets containing information about specific meteors sighted and is provided by the Meteorical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g). The scripts included in this project are:
- ```Dockerfile```
- ```app.py```
There are additionally five yaml files which when used on a Kubernetes cluster create the environment necessary to interact with the API:
-```s-shah-test-redis-deployment.yml```
-```s-shah-test-redis-pvc.yml```
-```s-shah-test-redis-service.yml```
-```s-shah-test-redis-deployment.yml```
-```s-shah-test-flask-service.yml```
