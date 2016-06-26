chimera-schneiderotb plugin
===========================

This plugin makes a Schneider Electric Advantys OTB Ethernet network I/O module a chimera switch to, for example,
switch lamps and fans.


Installation
------------

This plugin depends on `pymodbus`_ to connect to the controller.

::

    pip install -U git+https://github.com/astroufsc/chimera-schneiderotb.git


Configuration Example
---------------------

Examples of the configuration to be added on ``chimera.config`` file:

::

    switches:

        - name: dome_lamp
          type: SchneiderOTBSwitch
          device: 192.168.0.10
          output: 5

        - name: m1_fan
          type: SchneiderOTBSwitch
          device: 192.168.0.10
          output: 6

or

::

    lamps:

        - name: dome_lamp
          type: SchneiderOTBSwitch
          device: 192.168.0.10
          output: 5

    fans:

        - name: m1_fan
          type: SchneiderOTBSwitch
          device: 192.168.0.10
          output: 6


Tested Hardware
---------------

This plugin was tested on Schneider Electric Advantys OTB model OTB1E0DM9LP.


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-schneiderotb/

.. _pymodbus: https://pypi.python.org/pypi/pymodbus