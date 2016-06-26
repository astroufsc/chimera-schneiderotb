from chimera.core.chimeraobject import ChimeraObject
from chimera.interfaces.fan import Fan
from chimera.interfaces.lamp import Lamp
from chimera.interfaces.switch import Switch
from pymodbus.client.sync import ModbusTcpClient


class SchneiderOTBSwitch(ChimeraObject, Switch):
    __config__ = {"device": None,
                  "output": 6,  # Which output to switch on/off
                  "switch_timeout": None,  # Maximum number of seconds to wait for state change
                  }

    def __init__(self):
        super(SchneiderOTBSwitch, self).__init__()

    def __start__(self):
        self.client = ModbusTcpClient(self["device"])

    def _getOTBstate(self):
        return self.client.read_holding_registers(100).getRegister(0)

    def _setOTBstate(self, state):
        self.client.write_register(100, state)
        return True

    def switchOn(self):
        if not self.isSwitchedOn():
            if self._setOTBstate(self._getOTBstate() + (1 << self['output'])):
                self.switchedOn()
                return True
            else:
                return False

    def switchOff(self):
        if self.isSwitchedOn():
            if self._setOTBstate(self._getOTBstate() - (1 << self['output'])):
                self.switchedOff()
                return True
            else:
                return False

    def isSwitchedOn(self):
        return self._getOTBstate() & 1 << self['output'] != 0


if __name__ == '__main__':
    s = SchneiderOTBSwitch()
    print 'Switched on?', s.isSwitchedOn()
    print 'Switching on.'
    s.switchOn()
    print 'Switched on?', s.isSwitchedOn()
    print 'Switching off.'
    s.switchOff()
    print 'Switched on?', s.isSwitchedOn()
