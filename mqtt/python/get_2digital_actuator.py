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


PROJECT_ID = 'paste_your_PROJECT_ID_here'
DEVICE_UUID = 'paste_your_DEVICE_UUID_here'
API_KEY = 'paste_your_API_KEY_here'
ACTUATOR_NAME_1 = 'paste_your_first_ACTUATOR_NAME_here'
ACTUATOR_NAME_2 = 'paste_your_second_ACTUATOR_NAME_here'


def on_actuator_1(data):
    """
    Whenever an actuator receives a command from DeviceHub.net, it's state property is updated.
    The received data is also passed to the callback as a dictionary consisting of 'timestamp' and 'state'.
    timestamp - contains the unix timestamp at which the actuator was commanded
    state - contains the new actuator state
    """
    print 'Received command to toggle the LED to', ACTUATOR_1.state


def on_actuator_2(data):
    print 'Received command to set the servo to', ACTUATOR_2.state


# We want the data to be saved to disk before sending it to DeviceHub.net so we're setting persistent to True
# This also ensures that the project data stored locally is loaded if it exists.
project = Project(PROJECT_ID, persistent=True)
device = Device(project, DEVICE_UUID, API_KEY)


ACTUATOR_1 = Actuator(Actuator.DIGITAL, ACTUATOR_NAME_1)
ACTUATOR_2 = Actuator(Actuator.ANALOG, ACTUATOR_NAME_2)


device.addActuator(ACTUATOR_1, on_actuator_1)
device.addActuator(ACTUATOR_2, on_actuator_2)

while True:
    device.send()
    sleep(1)