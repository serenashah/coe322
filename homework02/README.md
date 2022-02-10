# Meteorite Site Investigation Journey
This project is comprised of two scripts which simulate a robotic vehicle on Mars tasked with investigating meteorite landing sites in Syrtis Major. The simulation gives the user an idea of the journey of the vehicle probing and sampling various sites, providing a fairly accurate time approximation for the full journey of the vehicle.

## Site Generator: generate_sites.py
One program both generates random coordinates in the region (16.0-18.0 degrees North and 82.0-84.0 degrees East) for 5 sites, and randomly chooses a meteorite composition to pair with it, and then creates a .json data file, site_data.json, for these sites. 

## Trip Calculator: calculate_trip.py
The second program reads this data file and and calculates the distance of the robot tracing the path from site to site in order of the data. It accounts for the time to sample the site based on the composition of the respective meteorite and outputs data for each leg of the trip about its travel and sampling time until the trip is over.

## Usage
To generate the site_data.json data file with the randomized Syrtis Major site information, run the generate_sites.py script in terminal with ```python3 generate_sites.py```
To read the data from the data file and simulate the vehicle's journey over the span of the sites, run the calculate_trip.py script in terminal with ```python3 calculate_trips.py``` 