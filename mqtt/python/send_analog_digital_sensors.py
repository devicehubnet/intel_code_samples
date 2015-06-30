"""

DeviceHUB.net sample code for sending an analog sensor and a digital sensor.

In this example the sensors are random simulated.

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 30 June 2015
by Mihnea Moldovan

"""


from devicehub.devicehub import Sensor, Actuator, Device, Project
from random import randint
from time import sleep


PROJECT_ID = 'paste_your_PROJECT_ID_here'
DEVICE_UUID = 'paste_your_DEVICE_UUID_here'
API_KEY = 'paste_your_API_KEY_here'
AN_SENSOR_NAME = 'paste_your_analog_SENSOR_NAME_here'
DI_SENSOR_NAME = 'paste_your_digital_SENSOR_NAME_here'



project = Project(PROJECT_ID, persistent = True)
device = Device(project, DEVICE_UUID, API_KEY)

DI_SENSOR = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME)
AN_SENSOR = Sensor(Sensor.ANALOG, AN_SENSOR_NAME)

device.addSensor(DI_SENSOR)
device.addSensor(AN_SENSOR)


while True:
    DI_SENSOR.addValue(randint(0, 1))
    sleep(0.5)
    AN_SENSOR.addValue(randint(1, 100))
    device.send()
    sleep(1)