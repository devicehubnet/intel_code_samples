"""

DeviceHUB.net sample code for sending a string.

In this example the string is simulated.

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 12 May 2017
by Gabriel Arnautu

"""


from devicehub.devicehub import Sensor, Actuator, Device, Project
from random import randint
from time import sleep


PROJECT_ID = '13156'
DEVICE_UUID = '9e4f6a13-ab95-42ab-81c8-a857864f2891'
API_KEY = '209b0ec1-d2ef-4d01-b915-81688b540bfc'


HELLO_WORLD_STRING = 'Hello_World_Sensor'


project = Project(PROJECT_ID, persistent = False)
device = Device(project, DEVICE_UUID, API_KEY)


HELLO_SENSOR = Sensor(Sensor.STRING, HELLO_WORLD_STRING)

device.addSensor(HELLO_SENSOR)


while True:
	HELLO_SENSOR.addValue("Hello World from Intel Edison")
	device.send()
	sleep(10)