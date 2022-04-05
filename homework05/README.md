# Meteorite Landing Database Server
This project allows users to load and receive datasets containing information about specific meteors sighted and is provided by the Meteorical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g). The scripts included in this project are:
- ```Dockerfile```: Downloads necessary dependencies and environment variables for the Flask application.
- ```app.py```: Provides routes to download and return the Meteorite Landings data set.  
## Downlaoding the Meteorite Landings Dataset
To access the meteorite landings dataset you can download it to your project directory with the following command:
```bash
[user@f5p ~]$ wget 
```
## Running the Redis Server
It uses a containerized Redis database server to provide access to the default Redis port inside the container from the host. 

## Running the Flask Container
It then uses a containerized Flask application to provide access to the default Flask port from the host. 
