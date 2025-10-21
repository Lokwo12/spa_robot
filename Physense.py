"""
physical sensor api process

input: data from the world
output: physical sensor signals

"""
from typing  import Any
import json
from bottle import route, run
from time import sleep


class PhySensor:
    
    """Abstract class for physical class"""
    def __init__(self, name: str, working_range: tuple, config_file: str = ""):
        assert isinstance(name, str) and len(name) > 0, "name must be a non-empty string"
        assert isinstance(working_range, tuple) and len(working_range) == 2, "working_range must be a tuple of (min, max)"
        assert isinstance(config_file, str), "config_file must be a string"
        
        self.name = name
        self.working_range = working_range
        self.config_file = config_file
        
    def read(self) -> Any:
        """Read sensor value - to be implemented by subclasses"""
        raise NotImplementedError


class DistanceSensor(PhySensor):
    
    """proximity distance sensor """
  
    def read(self) -> float:
        """Simulate reading a distance value"""
        import random
        return random.uniform(self.working_range[0], self.working_range[1])




if __name__ == "__main__":
    as1 = PhySensor("test_sensor", (-1, 1), "test.json")
    print(as1)
    
@route('/read_distance_sensor/<sensor_name>')
def read_distance_sensor(sensor_name: str) -> str:
    
    # create a distance sensor with a default range and return JSON distance
    sensor = DistanceSensor(sensor_name, (0.0, 10.0))
    value = sensor.read()
    return json.dumps({"sensor": sensor_name, "distance": value})

import urllib.request
import threading

def _start_server():
    run(host='localhost', port=8080)

if __name__ == "__main__":
    server_thread = threading.Thread(target=_start_server, daemon=True)
    server_thread.start()
    sleep(0.1)  # give server time to start

    try:
        with urllib.request.urlopen('http://localhost:8080/read_distance_sensor/distance_sensor_1') as resp:
            ds1_value = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        ds1_value = {"error": str(e)}

    print("I have an HTTP response:", ds1_value)
    print(ds1_value)
    sleep(0.1) # simulate periodic reading of sensor data
    
if __name__ == "__main__":
    """"
    1 define the route
    read sensor
    3.make percetions
    distance <10 cm -> close object
    """
sleep(1)  # keep the main thread alive for a while to allow server interaction