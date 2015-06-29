"""

DeviceHUB.net sample code for sending 2 strings.

In this example the strings are simulated.

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
STRING_NAME_1 = 'paste_your_first_STRING_NAME_here'
STRING_NAME_2 = 'paste_your_second_STRING_NAME_here'


#string simulation
data1 = "StringTest1"
data2 = "StringTest2"

project = Project(PROJECT_ID, persistent = True)
device = Device(project, DEVICE_UUID, API_KEY)

STR1 = Sensor(Sensor.STRING, STRING_NAME_1)
STR2 = Sensor(Sensor.STRING, STRING_NAME_2)

device.addSensor(STR1)
device.addSensor(STR2)


while True:
    STR1.addValue(data1)
    STR2.addValue(data2)
    device.send()
    sleep(1)