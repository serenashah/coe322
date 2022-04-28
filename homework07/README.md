# ISS Data Querier
The ISS Data Querier application provides this functionality as a containerized web application so that a user in interest of the ISS can query and access specific information about the spacecraft from the extensive data sets provided by NASA’s JSC. As the third brightest object in the sky, the ISS is a celestial object of significant esteem, and its whereabouts and conditions prove intriguing to thousands of space-lovers around the world. This project offers users the ability to sift through abundant amounts of data about the International Space Station (ISS) and easily access specific information about the ISS (including its position, velocity, and various sightings of the spacecraft across the world) using a containerized Flask web application.

## Diagram Explication
The following diagram visually models the functionality of the ISS Data Querier project, detailing user actions required to retrieve specific information about the International Space Station:
![Diagram](COE332_Midterm_Diagram.pdf)

The user must first create a running container of the Flask web server hosting the application. This has been made simple with the ```make all``` command, which creates all targets listed in the Makefile, creating an environment with all necessary dependencies and variables to run the application.

From there the user loads the datasets (that should be downloaded to their repository) onto the application with an HTTP ```-X POST``` verb, ```curl```ing to the route ```/data```. Now the data can be queried.

To retrieve any sort of information, the user must use the HTTP ```GET``` verb, which doesn't require being explicitly typed. Two types of data can be accessed (either the positional data or the sighting data), and these can be accessed through either the ```epoch``` routes or ```countries``` routes, respectively. The "Specific <Epoch/Country/City/Region> Data" blocks are routes with detailed information on all the sightings of the specified area. The route blocks with titles (i.e. "Epochs", "Countries", etc.) return lists of the respective regions with sightings.

The labels on the arrows indicate actions for the users to take when utilizing the application. Red blocks indicate HTTP commands, and all blocks within the "Positional Data Routes" and "Sighting Data Routes" borders indicate application functionalities that are called through specific routes.

## Project Access
Further detail about the project's implementation can be found at this [GitHub repository](https://github.com/serenashah/iss-tracking.git), including informatioin about:
- the ISS positional and sighting data sets
- the container of the application
- the commands to run the application
- the routes of the application
