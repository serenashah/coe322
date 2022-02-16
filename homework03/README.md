# Water Turbidity Analysis
This project is comprised of two scripts and analyzes a .json file, ```turbidity_data.json```, containing data in a time series list of dictionaries on the characteristics of some water sample quality. It then provides information on the average turbidity (relative clarity) of the 5 most recent measurements, and if this is over the desire turbidity threshold of 1.0 NTU, it returns the minimum amount of itme for the water to fall below the threshold.

## Downloading turbidity_data.json
To download the turbidity data set to analyze, type ```wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json``` into the command line of your terminal.   
Or visit this [link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) and copy and paste the data into a .json file of your own. Ensure that the file is in the same repository as the scripts so that the file can be accessed by the programs.
## Scripts
### Analyzing the Water: analyze_water.py
This program reads the turbidity data file and parses it. One function iterates through the data file list and calculates the turbidity, **T**, of the sample using information about its calibration constant, **a0**, and its detector current **I90**. The main function calculates the average of the five most recent turbidities, and this number is inputted into the second function which returns the time to fall below a safe turbidity threshold, **Ts = 1.0 NTU**, considering variables of decay factor per hour, **d = 0.02**, and the inputted current turbidity, **T0 = T**.  

### Testing the Analysis Script: test_analyze_water.py
This program is a unit test script that verifies the performance of the functions in the program analyzing the water. Both functions each have various tests for their accuracy and for exceptions in the case of invalid inputs, with 5 assertions for each.

## Usage
To find the average turbidity of the most recent 5 measurements and get information about the time for the water to fall below the turbidity threshold, run the analyze_water.py script in terminal with ```python3 analyze_water.py```.  
To test the turbidity and time calculations, run the test_analyze_water.py test in terminal with ```pytest test_analyze_water.py```.  
Running the analyze_water.py script will give you labeled information about the average turbidity of the 5 most recent measurements, whether or not this is within the safe threshold, and how long until the water will reach this level.
Running the test_analyze_water.py script will display a green . for every passed function and an F for the failed functions. If you see all green that means the functions are performing correctly.