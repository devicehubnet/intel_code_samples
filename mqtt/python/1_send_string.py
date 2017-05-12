"""

DeviceHUB.net sample code for sending a string.

In this example the string is simulated.

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 29 June 2015
by Mihnea Moldovan

"""


from devicehub.devicehub import Sensor, Actuator, Device, Project
from random import randint
from time import sleep


PROJECT_ID = 'paste_your_PROJECT_ID_here'
DEVICE_UUID = 'paste_your_DEVICE_UUID_here'
API_KEY = 'paste_your_API_KEY_here'
STRING_NAME = 'paste_your_STRING_NAME_here'

#string simulation
data = "StringTest"

project = Project(PROJECT_ID, persistent = True)
device = Device(project, DEVICE_UUID, API_KEY)

STR = Sensor(Sensor.STRING, STRING_NAME)

device.addSensor(STR)


while True:
    STR.addValue(data)
    device.send()
    sleep(1)