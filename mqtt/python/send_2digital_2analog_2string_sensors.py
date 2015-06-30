"""

DeviceHUB.net sample code for sending 2 digital + 2 analog sensors and 2 strings.

In this example the sensors and strings are simulated.

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
DI_SENSOR_NAME_1 = 'paste_your_first_digital_SENSOR_NAME_here'
DI_SENSOR_NAME_2 = 'paste_your_second_digital_SENSOR_NAME_here'
AN_SENSOR_NAME_1 = 'paste_your_first_analog_SENSOR_NAME_here'
AN_SENSOR_NAME_2 = 'paste_your_second_analog_SENSOR_NAME_here'
STRING_NAME_1 = 'paste_your_first_STRING_NAME_here'
STRING_NAME_2 = 'paste_your_second_STRING_NAME_here'

#string simulation
data_1 = "StringTest"
data_2 = "StringTest"

project = Project(PROJECT_ID, persistent = True)
device = Device(project, DEVICE_UUID, API_KEY)

DI_SENSOR_1 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME_1)
DI_SENSOR_2 = Sensor(Sensor.DIGITAL, DI_SENSOR_NAME_2)
AN_SENSOR_1 = Sensor(Sensor.ANALOG, AN_SENSOR_NAME_1)
AN_SENSOR_2 = Sensor(Sensor.ANALOG, AN_SENSOR_NAME_2)
STR_1 = Sensor(Sensor.STRING, STRING_NAME_1)
STR_2 = Sensor(Sensor.STRING, STRING_NAME_2)

device.addSensor(DI_SENSOR_1)
device.addSensor(DI_SENSOR_2)
device.addSensor(AN_SENSOR_1)
device.addSensor(AN_SENSOR_2)
device.addSensor(STR_1)
device.addSensor(STR_2)


while True:
    DI_SENSOR_1.addValue(randint(0, 1)) #sensor random simulation
    sleep(0.5)
    DI_SENSOR_2.addValue(randint(0, 1))
    sleep(0.5)
    AN_SENSOR_1.addValue(randint(1, 100))
    sleep(0.5)
    AN_SENSOR_2.addValue(randint(1, 100))
    sleep(0.5)
    STR_1.addValue(data_1)
    sleep(0.5)
    STR_2.addValue(data_2)
    device.send()
    sleep(1)