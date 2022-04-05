# Meteorite Landing Database Server
This project allows users to load and receive datasets containing information about specific meteors sighted and is provided by the Meteorical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g). The scripts included in this project are:
- ```Dockerfile```: Downloads necessary dependencies and environment variables for the Flask application.
- ```app.py```: Provides routes to download and return the Meteorite Landings data set.  
## Downlaoding the Meteorite Landings Dataset
To access the meteorite landings dataset you can download it to your project directory with the following command:
```bash
[user@f5p ~]$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```
## Launching the Redis Database
The Redis database is containerized to provide access to the default Redis port inside the container from the host.
First pull the existing official image for Redis version 6 with:
```bash
[user@f5p ~]$ docker pull redis:6
```
The Redis database can be launched with Docker using the following command. 
```bash
[user@f5p ~]$ docker run -d -p 6428:6379 -v $(pwd)/data:/data:rw --name=serena-redis redis:6 --save 1 1
1:C 31 Mar 2021 16:48:11.939 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
...
1:M 31 Mar 2021 16:48:11.972 * Ready to accept connections
```
This runs the container in the background and mounts your local directory to the folder ```/data``` inside the container. It additionally configures the server to save 1 backup file every second.
## Running the Flask Container
The Flask application is also containerized to provide access to the default Flask port from the host. 
First pull the existing image for the Flask application with:
```bash
[user@f5p ~]$ docker pull serenashah/flask-redis:latest
```
You can then build the container with the following container, running it in the background:
```bash
[user@f5p ~]$ docker build -t serenashah/flask-redis:latest .
```
Then run your container:
```bash
[user@f5p ~]$ docker run --name "<container_name>" -d -p 5028:5000 serenashah/flask-redis latest
```
# Utilizing the Applicaition
The application contains two routes, both to the URL lcoation ```/data```.
The first is a ```POST``` route that can be accessed with the HTTP client ```curl```. Load your meteorite landing data to the application with the following command:
```bash
[user@f5p ~]$ curl -X POST localhost:5028/data
Data has been loaded.
```
To then receive a JSON list of your data that has been uploaded, use the following command:
```
[user@f5p ~]$ curl localhost:5028/data
```
Because the HTTP verb is ```GET```, it is not required to explicitly express the verb as done for ```POST``` with the tag ```-X```.

#### Enjoy!
