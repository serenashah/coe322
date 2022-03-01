# Meteorite Landings Data Analaysis
This project offers various analyses on unique features of a comprehensive meteorite landings data set provided by The Meteoritical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g).  
The project includes:
- An example data set: ```Meteorite_Landing.json```
- A script that provides a summary of the analysis of the data set: ```ml_data_analysis.py```
- A testing script for the analytical script: ```test_ml_data_analysis.py```
- A ```Dockerfile``` to run the programs in a container with the required/recommended base image and dependencies

## Main Scripts
### Meteorite Landings Data Set: ```Meteorite_Landing.json```
This comprehensive data set consists of unique features of various meteorite landings and is provided by The Meteoritical Society. Meteorite features used for analysis include class, longitude, latitude, and mass (g).

### Meteorite Landings Data Analysis Script: ```ml_data_analysis.py```
This script consists of many functions that offer particular information on the data collectively. Its output specifically offers information on the meteorites' average mass, number of meteorites per hemisphere, and number of respective class type.

### Data Analysis Tester Script: ```test_ml_data_analysis.py```
This testing script tests the accuracy and the functionality of the functions of the analysis script, ```ml_data_analaysis.py```. Tests include key errors, value errors, type errors of the ```compute_average_mass```, ```check_hemisphere```, and ```count_class``` functions. To run the script in terminal, enter the following:  
```pytest test_ml_data_analysis.py```
