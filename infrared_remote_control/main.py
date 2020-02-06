#!/usr/bin/env python3

#from pybricks import ev3brick as brick
import ev3dev2
from ControlCar import ControlCar
from ev3dev2.motor import OUTPUT_A, OUTPUT_D
import time

# Write your program here
#brick.sound.beep()

control_car = ControlCar(OUTPUT_A, OUTPUT_D, 'IR-REMOTE')

while True:
    control_car.process()
    #time.sleep(1)