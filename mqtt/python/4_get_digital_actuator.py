"""

DeviceHUB.net sample code for getting an digital actuator and switch a relay.

In this example the sensors are random simulated.

First install Python API wrapper for devicehub 
https://github.com/devicehubnet/devicehub_py

created 30 June 2015
by Mihnea Moldovan

"""


from devicehub.devicehub import Sensor, Actuator, Device, Project
from random import randint
from time import sleep
import mraa


PROJECT_ID = '13156'
DEVICE_UUID = '9e4f6a13-ab95-42ab-81c8-a857864f2891'
API_KEY = '209b0ec1-d2ef-4d01-b915-81688b540bfc'


BUZZER_DIGITAL_ACTUATOR_NAME = "Buzzer_power"

buzzer_power_port = mraa.Gpio(3)
buzzer_power_port.dir(mraa.DIR_OUT)

def on_actuator_change(data):
    buzzer_power_port.write(int(BUZZER_ACTUATOR.state))


project = Project(PROJECT_ID, persistent = False)
device = Device(project, DEVICE_UUID, API_KEY)


BUZZER_ACTUATOR = Actuator(Actuator.DIGITAL, BUZZER_DIGITAL_ACTUATOR_NAME)
device.addActuator(BUZZER_ACTUATOR, on_actuator_change)


while True:
    sleep(1)
