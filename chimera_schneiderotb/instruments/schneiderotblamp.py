from chimera.interfaces.lamp import Lamp
from chimera_schneiderotb.instruments.schneiderotbswitch import SchneiderOTBSwitch


class SchneiderOTBLamp(Lamp, SchneiderOTBSwitch):
    def __init__(self):
        super(SchneiderOTBLamp, self).__init__()
