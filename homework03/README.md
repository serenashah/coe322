# Water Turbidity Analysis
This project is comprised of two scripts and analyzes a .json file, ```turbidity_data.json```, containing data in a time series list of dictionaries on the characteristics of some water sample quality. It then provides information on the average turbidity (relative clarity) of the 5 most recent measurements, and if this is over the desire turbidity threshold of 1.0 NTU, it returns the minimum amount of itme for the water to fall below the threshold.

## Downloading turbidity_data.json
To download the ```turbidity_data.json``` data set to analyze, type ```wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json``` into the command line of your terminal.
Or visit this [link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) and copy and paste the data into a .json file of your own. Ensure that the file is in the same repository as the scripts.

## Analyzing the Water: analyze_water.py

## Testing the Analysis Script: test_analyze_water.py
To calculate 

## Usage
To find the average turbidity of the most recent 5 measurements and get information about the time for the water to fall below the turbidity threshold, run the analyze_water.py script in terminal with ```python3 analyze_water.py```. To test the turbidity and time calculations, run the test_analyze_water.py test in terminal with ```pytest test_analyze_water.py```.