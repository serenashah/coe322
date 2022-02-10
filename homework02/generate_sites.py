import random

def lat():
    """
    Generates a random float between 16.0 and 18.0 for latitude.
    """
    return (random.uniform(16.0, 18.0))
def lon():
    """
    Generates a random float between 82.0 and 84.0 for longitude.
    """
    return (random.uniform(82.0, 84.0))
def comp():
    """
    Randomly returns one out of three strings.
    """
    ran_num = random.randrange(1, 4)
    if (ran_num == 1):
        return('stony')
    if (ran_num == 2):
        return('iron')
    if (ran_num == 3):
        return('stony-iron')

def main():
    import json

    site_data ={}
    site_data['sites'] = []

    for x in range(5):
        site_data['sites'].append( {'site_id' : x+1, 'latitude' : lat(), 'longitude' : lon(), 'composition' : comp()})

    with open('site_data.json', 'w' ) as out:
        json.dump(site_data, out, indent = 2)

if __name__ == '__main__':
    main()
