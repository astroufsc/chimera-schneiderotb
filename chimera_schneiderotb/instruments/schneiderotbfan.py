from chimera.interfaces.fan import Fan
from chimera_schneiderotb.instruments.schneiderotbswitch import SchneiderOTBSwitch


class SchneiderOTBFan(Fan, SchneiderOTBSwitch):
    def __init__(self):
        super(SchneiderOTBFan, self).__init__()
