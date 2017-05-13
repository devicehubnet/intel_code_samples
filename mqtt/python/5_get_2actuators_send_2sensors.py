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
BUZZER_ANALOG_ACTUATOR_NAME = "Buzzer_intensity"


buzzer_pwm_port = mraa.Pwm(3)
buzzer_pwm_port.dir(mraa.DIR_OUT)


def on_digital_actuator_change(data):
    print "digital", BUZZER_ACTUATOR.state
    buzzer_pwm_port.enable(bool(BUZZER_ACTUATOR.state))

def on_analog_actuator_change(data):
    print "analog", BUZZER_ANALOG.state
    pass

project = Project(PROJECT_ID, persistent = False)
device = Device(project, DEVICE_UUID, API_KEY)


BUZZER_ACTUATOR = Actuator(Actuator.DIGITAL, BUZZER_DIGITAL_ACTUATOR_NAME)
device.addActuator(BUZZER_ACTUATOR, on_digital_actuator_change)
BUZZER_ANALOG = Actuator(Actuator.ANALOG, BUZZER_ANALOG_ACTUATOR_NAME)
device.addActuator(BUZZER_ACTUATOR, on_analog_actuator_change)


while True:
    sleep(1)