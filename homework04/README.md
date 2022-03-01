# Meteorite Landings Data Analaysis
This project offers various analyses on unique features of a comprehensive meteorite landings data set provided by The Meteoritical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g).  
The project includes:
- An example data set: ```Meteorite_Landing.json```
- A script that provides a summary of the analysis of the data set: ```ml_data_analysis.py```
- A test suite for the analytical script: ```test_ml_data_analysis.py```
- A ```Dockerfile``` to run the programs in a container with the required/recommended base image and dependencies

## Main Scripts
### Meteorite Landings Data Set: ```Meteorite_Landing.json```
This comprehensive data set consists of unique features of various meteorite landings and is provided by The Meteoritical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g).

### Meteorite Landings Data Analysis Script: ```ml_data_analysis.py```
This script consists of many functions that offer particular information on the data collectively. Its output specifically offers information on the meteorites' average mass, number of meteorites per hemisphere, and number of respective class type.

### Data Analysis Test Suite: ```test_ml_data_analysis.py```
This testing script tests the accuracy and the functionality of the functions of the analysis script, ```ml_data_analaysis.py```. Tests include key errors, value errors, type errors of the ```compute_average_mass```, ```check_hemisphere```, and ```count_class``` functions. 

## Docker Usage
To run these scripts in an environment that has the necessary and recommended dependencies, environment variables, base image, and install processes, run these scripts in the 
created ml_data_analysis Docker container.
#### Pulling or Building an Image
To have a functioning image to run your scripts in, you can either pull an existing image from Docker Hub, or build your own image. 
To pull the image from the Docker Hub repository, run the following command in terminal:  
```bash
[user@f5p ~]$ docker pull serenashah/ml_data_analysis:hw04 
```
> Expected first line output: 
```sh
hw04: Pulling from serenashah/ml_data_analysis
...
```   
To build your own image of the container, run the following command in terminal:
```sh
[user@f5p ~]$ docker build -t serenashah/ml_data_analysis:hw04 .
```
> Expected first two lines output (should continue for 8 steps): 
```sh
Sending build context to Docker daemon  34.82kB
Step 1/8 : FROM centos:7.9.2009
...
```  
#### Running the code inside the Container
Run the follow command in terminal to enter the container:
```sh
[user@f5p ~]$ docker run --rm -it serenashah/ml_data_analysis:hw04 /bin/bash
```
Once in the container, your user should change from your desktop username to a root user, and you can find the three main scripts listed in the code repository. 
```sh 
[root@6bc7d8bd0d18]# ls/code
```
> Expected output: 
```sh
Meteorite_Landings.json  ml_data_analysis.py  test_ml_data_analysis.py
```
To run the ```ml_data_analysis.py``` script with the provided ```Meteorite_Landings.json``` data set run the following in the ```code``` repository.
```sh
[root@6bc7d8bd0d18 code]# ./ml_data_analysis.py Meteorite_Landings.json
```
> The output should resemble a summary of the following information (numbers may be subject to change depending on version of data set):
```bash 
Summary data following meteorite analysis:

Average mass of 30 meteor(s):
83857.3

Hemisphere summary data:
There were 21 meteors found in the Northern & Eastern quadrant
There were 0 meteors found in the Southern & Eastern quadrant
There were 6 meteors found in the Northern & Western quadrant
There were 3 meteors found in the Southern & Western quadrant

 Class summary data:
The L5 class was found 1 times
The H6 class was found 1 times
The EH4 class was found 2 times
The Acapulcoite class was found 1 times
...
```
