#Meteorite Site Investigation
This project is comprised of two scripts which simulate a robotic vehicle on Mars tasked with investigating meteorite landing sites in Syrtis Major.

##generate_sites.py
One program both generates random coordinates in the region (16.0-18.0 degrees North and 82.0-84.0 degrees East) for 5 sites, and randomly chooses a meteorite composition to pair with it, and then creates a .json data file for these sites. 

##calculate_trip.py
The second program reads this data file and and calculates the distance of the robot tracing the path from site to site in order of the data. It accounts for the time to sample the site based on the composition of the respective meteorite and outputs data for each leg of the trip about its travel and sampling time until the trip is over.