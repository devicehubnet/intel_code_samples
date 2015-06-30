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
ACTUATOR_NAME = 'paste_your_ACTUATOR_NAME_here'


def on_actuator(data):
    """
    Whenever an actuator receives a command from DeviceHub.net, it's state property is updated.
    The received data is also passed to the callback as a dictionary consisting of 'timestamp' and 'state'.
    timestamp - contains the unix timestamp at which the actuator was commanded
    state - contains the new actuator state
    """
    print 'Received command to toggle the LED to', ACTUATOR.state



# We want the data to be saved to disk before sending it to DeviceHub.net so we're setting persistent to True
# This also ensures that the project data stored locally is loaded if it exists.
project = Project(PROJECT_ID, persistent=True)
device = Device(project, DEVICE_UUID, API_KEY)


ACTUATOR = Actuator(Actuator.DIGITAL, ACTUATOR_NAME)


device.addActuator(ACTUATOR, on_actuator)