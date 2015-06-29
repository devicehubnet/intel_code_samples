"""

DeviceHUB.net sample code for sending 2 digital sensors.

In this example the sensors are random simulated.

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
DI_SENSOR_NAME_1 = 'paste_your_first_digital_SENSOR_NAME_here'
DI_SENSOR_NAME_2 = 'paste_your_second_digital_SENSOR_NAME_here'



project = Project(PROJECT_ID, persistent = True)
device = Device(project, DEVICE_UUID, API_KEY)

DI_SENSOR_1 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME_1)
DI_SENSOR_2 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME_2)

device.addSensor(DI_SENSOR_1)
device.addSensor(DI_SENSOR_2)


while True:
    DI_SENSOR_1.addValue(randint(0, 1))
    sleep(0.5)
    DI_SENSOR_1.addValue(randint(0,1))
    device.send()
    sleep(1)