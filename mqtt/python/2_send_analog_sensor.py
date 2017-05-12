"""

DeviceHUB.net sample code for sending an analog sensor.

In this example the sensor is random simulated.

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 12 May 2017
by Gabriel Arnautu

"""


from devicehub.devicehub import Sensor, Actuator, Device, Project
from random import randint
from time import sleep
import mraa


PROJECT_ID = '13156'
DEVICE_UUID = '9e4f6a13-ab95-42ab-81c8-a857864f2891'
API_KEY = '209b0ec1-d2ef-4d01-b915-81688b540bfc'


TEMPERATURE_SENSOR_NAME = 'Temperature'


project = Project(PROJECT_ID, persistent = False)
device = Device(project, DEVICE_UUID, API_KEY)


TEMPERATURE_SENSOR = Sensor(Sensor.STRING, TEMPERATURE_SENSOR_NAME)

device.addSensor(TEMPERATURE_SENSOR)


while True:
	TEMPERATURE_SENSOR.addValue(20)
	device.send()
	sleep(10)