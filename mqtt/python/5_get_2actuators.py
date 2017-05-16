"""

DeviceHUB.net sample code for getting an digital actuator and switch a relay.

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


BUZZER_DIGITAL_ACTUATOR_NAME = "Buzzer_power"
BUZZER_ANALOG_ACTUATOR_NAME = "Buzzer_intensity"


buzzer_pwm_port = mraa.Pwm(3)
buzzer_pwm_port.enable(True)
buzzer_pwm_port.write(1.0)

def on_digital_actuator_change(data):
    buzzer_pwm_port.enable(bool(int(BUZZER_ACTUATOR.state)))

def on_analog_actuator_change(data):
    value = float(BUZZER_ANALOG.state)/100.0
    buzzer_pwm_port.write(value)


project = Project(PROJECT_ID, persistent = False)
device = Device(project, DEVICE_UUID, API_KEY)


BUZZER_ACTUATOR = Actuator(Actuator.DIGITAL, BUZZER_DIGITAL_ACTUATOR_NAME)
device.addActuator(BUZZER_ACTUATOR, on_digital_actuator_change)
BUZZER_ANALOG = Actuator(Actuator.ANALOG, BUZZER_ANALOG_ACTUATOR_NAME)
device.addActuator(BUZZER_ANALOG, on_analog_actuator_change)


while True:
    sleep(1)
