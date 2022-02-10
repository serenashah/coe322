def new_lat(site_dict, lat_string, site_num):
    return(site_dict[site_num-1][lat_string])

def new_lon(site_dict, lon_string, site_num):
    return(site_dict[site_num-1][lon_string])

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    import math
    mars_radius = 3389.5    # km
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def sample(site_dict, comp_string, site_num):
    if(site_dict[site_num-1][comp_string] == 'stony'):
        return(1)
    if(site_dict[site_num-1][comp_string] == 'iron'):
        return(2)
    if(site_dict[site_num-1][comp_string] == 'stony-iron'):
        return(3)

def travel(distance):
    time = distance/ 10
    return(time)

def main():
    import json

    with open('site_data.json', 'r') as f:
        read_sites = json.load(f)

    rob_lat1 = 16.0
    rob_lon1 = 82.0
    total_time = 0
    for i in range(1, len(read_sites['sites'])+1):
        rob_lat2 = (new_lat(read_sites['sites'], 'latitude', i))
        rob_lon2 = (new_lon(read_sites['sites'], 'longitude', i))
        distance = calc_gcd(rob_lat1, rob_lon1, rob_lat2, rob_lon2)
        travel_time = travel(distance)
        sample_time = sample(read_sites['sites'], 'composition', i)
        print("leg", i, ", time to travel:", travel_time, "hr, time to sample:", sample_time, "hr")
        rob_lat1 = rob_lat2
        rob_lon1 = rob_lon2
        total_time = total_time + sample_time + travel_time
    print("legs:", i, ", total time elapsed: ", total_time)


if __name__ == '__main__':
    main()
