from w1thermsensor import W1ThermSensor, Unit, Sensor
from time import time

def get_temperature():
    """
    Returns an array of dictionaries, each entry will correspond to data from a sensor DS18B20.
    {'id':SENSOR_ID, 'temp':TEMPERATURE_C, 'datetime':DATETIME}
    """ 
    out=[]
    for sensor in W1ThermSensor.get_available_sensors([Sensor.DS18B20]):
         dict_sensor={'id':sensor.id, 'temp':sensor.get_temperature(), 'datetime': int(time())}
         out.append(dict_sensor)
    return out
    