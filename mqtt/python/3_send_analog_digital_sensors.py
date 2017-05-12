"""

DeviceHUB.net sample code for sending an analog sensor and a digital sensor.

In this example the sensors are random simulated.

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


POTENTIOMETER_SENSOR_NAME = 'Potentiometer'
PUSH_BUTTON_NAME = 'Push_button'


project = Project(PROJECT_ID, persistent = False)
device = Device(project, DEVICE_UUID, API_KEY)


POTENTIOMETER_SENSOR = Sensor(Sensor.ANALOG, POTENTIOMETER_SENSOR_NAME)
PUSH_BUTTON_SENSOR = Sensor(Sensor.ANALOG, PUSH_BUTTON_NAME)

device.addSensor(POTENTIOMETER_SENSOR)
device.addSensor(PUSH_BUTTON_SENSOR)


potentiometer_port = mraa.Aio(0)
push_button_port = mraa.Gpio(2)
push_button_port.dir(mraa.DIR_IN)


while True:
	POTENTIOMETER_SENSOR.addValue(potentiometer_port.read())
	PUSH_BUTTON_SENSOR.addValue(push_button_port.read())
	device.send()
	sleep(3)