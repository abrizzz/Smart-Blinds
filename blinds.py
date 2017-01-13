#!/usr/bin/python3

import os
import RPi.GPIO as GPIO
import time
import sys
from enum import Enum

FILENAME="/home/pi/Projects/Smart-Blinds/status"

TIMEUP = 38
TIMEDOWN = 22

UP_SLOW = 7.5
UP_MED = 8
UP_FAST = 10

DOWN_SLOW = 6.5
DOWN_MED = 6
DOWN_FAST = 5

CLOSED = 0
OPENED = 1



class Blinds(object):
    """docstring for Blinds."""

    def read_status(self):
        saved_file=open(FILENAME, "r")
        self.status = float(saved_file.readline().strip())

    def write_status(self):
        saved_file=open(FILENAME, "w")
        saved_file.write(str(self.status))
        saved_file.close()

    def move(self,target):
        if(target > self.status):
            # Move Up by (target-self.status) * TIMEUP
            self.p.ChangeDutyCycle(UP_FAST)
            time.sleep(TIMEUP * (target-self.status))
        elif(target < self.status):
            # Move Down by (self.status-target) * TIMEDOWN
            self.p.ChangeDutyCycle(DOWN_FAST)
            time.sleep(TIMEDOWN * (self.status-target))
        self.p.stop()
        self.status = target
        self.write_status()

    def toggle(self):
        if (self.status == OPENED):
            self.move(0)
        elif (self.status == CLOSED):
            self.move(1)
        return self.status

    def cleanup(self):
        GPIO.cleanup()

    def __init__(self):
        super(Blinds, self).__init__()
        self.read_status()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.p = GPIO.PWM(18,50)
        self.p.start(7)

if __name__ == '__main__':
    b = Blinds()
    b.move(float(sys.argv[1]))
    b.cleanup()
