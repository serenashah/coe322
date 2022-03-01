#!/usr/bin/env python3
import json
from typing import List
import sys
import logging
import socket

format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)


def compute_average_mass(a_list_of_dicts: List[dict], a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value (will enforce float type).

    Returns:
        result (float): Average value.
    """
    if (len(a_list_of_dicts) == 0):
        logging.error('a list of dicts is empty')
    total_mass = 0.
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string])
    return(total_mass / len(a_list_of_dicts) )

def check_hemisphere(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude in decimal notation, returns which hemispheres
    those coordinates land in.

    Args:
        latitude (float): Latitude in decimal notation.
        longitude (float): Longitude in decimal notation.

    Returns:
        location (string): Short string listing two hemispheres.
    """
    if latitude == 0 or longitude == 0:
        #logging.error('youre not really in a hemisphere')
        raise(ValueError)
   
    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western'
    return(location)

def hemisphere_summary(n_e, s_e, n_w, s_w):
    print('There were', n_e, 'meteors found in the Northern & Eastern quadrant')
    print('There were', s_e, 'meteors found in the Southern & Eastern quadrant')
    print('There were', n_w, 'meteors found in the Northern & Western quadrant')    
    print('There were', s_w, 'meteors found in the Southern & Western quadrant')

def count_classes(a_list_of_dicts: List[dict], a_key_string: str) -> dict:
    """
    Iterates through a list of dictionaries, and pulls out the value associated
    with a given key. Counts the number of times each value occurs in the list of
    dictionaries and returns the result.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value.

    Returns:
        classes_observed (dict): Dictionary of class counts.

    """
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed:
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return(classes_observed)


def main():
    logging.debug('entering main loop')

    with open(sys.argv[1], 'r') as f:
        ml_data = json.load(f)

    logging.debug(f'the type of ml_data is {type(ml_data)}')

    print('Summary data following meteorite analysis: \n')
    print('Average mass of',  len(ml_data['meteorite_landings']),'meteor(s):')
    print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'),'\n')

    print('Hemisphere summary data:')
    n_e = 0; s_e = 0; s_w = 0; n_w = 0
    for row in ml_data['meteorite_landings']:
        locations = check_hemisphere(float(row['reclat']), float(row['reclong'])) 
        if (locations == 'Northern & Eastern'):
            n_e += 1
        if (locations == 'Southern & Eastern'):
            s_e += 1
        if (locations == 'Northern & Western'):
            n_w += 1
        if (locations == 'Southern & Western'):
            s_w += 1

    hemisphere_summary(n_e, s_e, n_w, s_w)
    print('\n', 'Class summary data:')
    for item in count_classes(ml_data['meteorite_landings'], 'recclass'):
        print('The', item, 'class was found', count_classes(ml_data['meteorite_landings'], 'recclass')[item], 'times')
    

if __name__ == '__main__':
    main()


