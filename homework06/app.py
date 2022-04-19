import redis
import json
from flask import Flask, request

app = Flask(__name__)

ml_data = {}
@app.route('/data', methods=['POST'])
def download_data(): 
    '''
    Opens and parses a json data file and loads it into a dictionary
        that can be used for all subsequent routes.

    Args: none
    Returns:
        A string to the client indicating that data has been downloaded.
    '''
    global ml_data

    with open('ML_Data_Sample.json', 'r') as f:
               ml_data = json.load(f)
    global rd
    rd = redis.Redis(host='10.98.212.79', port = 6379, db = 0)
    for d in ml_data['meteorite_landings']:
            rd.set(d['id'],json.dumps(d))

    
    return "Data has been loaded!\n"

@app.route('/data', methods=['GET'])
def load_redis():
    '''
    Returns a json list of the data loaded to the application.

    Args: none
    Returns:
        A JSON list of the information.
    '''   
    list_of_data = []
    
    for x in ml_data['meteorite_landings']:
        list_of_data.append(json.loads(rd.get(x['id'])))
    return (json.dumps(list_of_data, indent=1) + '\n')
    
if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
