#!/usr/bin/python3

""" Used to test servo rotation and for manual adjusments """

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18,50)

p.start(7)

i = 7
t = 0
while float(i) != -1:
  # time.sleep(5)
  p.ChangeDutyCycle(float(i))
  time.sleep(int(t))
  p.ChangeDutyCycle(7)
  i = input("Duty Cycle: ")
  t = input("Time: ")


p.stop()
GPIO.cleanup()
