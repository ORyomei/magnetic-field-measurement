from typing import List, Tuple
from pyvisa.resources.resource import Resource
from magnetic_field_measurement.init_ports import STEP_MOTOR_PORT
from enum import IntEnum
import pyvisa


class Direction(IntEnum):
    X = 0
    Y = 1


class StepperStatus(IntEnum):
    Idle = 0
    Busy = 0


class Stepper:
    ORIGIN_X = 5000  #TODO change
    ORIGIN_Y = 2000  #TODO change

    PULSESPERMILLIMETER = 100

    serial: Resource
    origin: List[int]
    coordinate: List[int]

    def __init__(self):
        self._serial_initialize()

    def _serial_initialize(self):
        rm = pyvisa.ResourceManager()
        self.serial = rm.open_resource(STEP_MOTOR_PORT)

    def moveRelative(self, pulse: int, dir: Direction):

        self.coordinate[dir] += pulse
        #TODO

    def moveAbsolute(self, coordinate: List[int]):
        for direction in Direction:
            pulse = coordinate[direction] - self.coordinate[direction]
            self.moveRelative(pulse, direction)
        self.coordinate = coordinate

    def setOrigin(self, originX: int = 0, originY: int = 0):
        self.origin = (originX, originY)

    def returnToOrigin(self):
        #TODO
        pass

    @property
    def coordinate(self) -> Tuple[int]:
        return self.coordinate

    @property
    def convertedCoordinate(self):
        return (self.coordinate[0] / Stepper.PULSESPERMILLIMETER,
                self.coordinate[1] / Stepper.PULSESPERMILLIMETER)

    @property
    def status(self):
        self.serial.write("R")
        for row in range(22):
            pass
        #TODO