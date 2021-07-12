from pyvisa.resources.resource import Resource
from magnetic_field_measurement.init_ports import DTM_151_PORT
import pyvisa


class SenserReceiver:

    serial: Resource

    def __init__(self):
        self._serial_initialize()

    def _serial_initialize(self):
        rm = pyvisa.ResourceManager()
        self.serial = rm.open_resource(DTM_151_PORT)

    def read(self):
        value = self.serial.query("F")
        return value