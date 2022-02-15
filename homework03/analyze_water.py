def calc_turb(turb_list: list, a0_string: str, I90_string: str, item: int) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with 
    two given keys for an item of the list. Returns the product of those values.
    """
    a0 = turb_list[item][a0_string]
    I90 = turb_list[item][I90_string]
    T = a0 * I90
    return(T)

def calc_time(T0: float) -> float:
    """
    Accepts an inputted float and returns a float value that is calculated using 
    this inputted variable.
    """
    import math
    Ts = 1.0 # NTU
    d = 0.02 # 2%
    b = math.log(Ts/T0) / math.log(1-d)
    return(b)

def main():
    import json

    with open('turb_data.json', 'r') as f:
        read_turb = json.load(f)

    total_turb = 0
    total_time = 0

    for x in range(5):
        current_turb = (calc_turb(read_turb['turbidity_data'], 'calibration_constant', 
                        'detector_current', x))
        total_turb = total_turb + current_turb
    
    avg_turb = total_turb / 5
    time = calc_time(avg_turb)
    print("Average turbidity on the five most recent measurements:", total_turb/5, "NTU")

    if avg_turb >= 1:
        print("Minimimum time required to return below a safe threshold =", time, "hrs")
    else:
        print("Minimimum time required to return below a safe threshold =", 0, "hrs")
        

if __name__ == '__main__':
    main()
