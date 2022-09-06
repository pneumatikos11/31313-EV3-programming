#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks.tools import wait
ev3_brick = EV3Brick()
left = Motor(Port.B)
right = Motor(Port.C)
move = DriveBase(left, right, 26, 102)
#from r3ptar import R3ptar


#r3ptar = R3ptar()

while True:
    move.drive(100,0)
    # r3ptar.drive_by_ir_beacon(speed=1000)
    # r3ptar.strike_by_ir_beacon(speed=1000)
    # r3ptar.hiss_if_touched()
    ev3_brick.speaker.play_file("Akwaaba.mp4")
    wait(1)

