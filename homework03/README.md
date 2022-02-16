# Water Turbidity Analysis
This project is comprised of two scripts and analyzes a .json file, ```turbidity_data.json```, containing data in a time series list of dictionaries on the characteristics of some water sample quality. It then provides information on the average turbidity (relative clarity) of the 5 most recent measurements, and if this is over the desire turbidity threshold of 1.0 NTU, it returns the minimum amount of itme for the water to fall below the threshold.

## Downloading turbidity_data.json
To download the ```turbidity_data.json``` data set to analyze, type the following command into the command line of your terminal:
```wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json``.
Or visit this [link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) and copy and paste the data into a .json file of your own.