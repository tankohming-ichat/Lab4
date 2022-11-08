import socket
import time
from time import sleep
import hal.hal_input_switch as switch
import hal.hal_led as led

switch.init()
led.init()
while True:
    if switch.read_slide_switch():
        led.set_output(24, 1)
        sleep(0.1)
        led.set_output(24, 0)
        sleep(0.1)
    else:
        for i in range(50):
            led.set_output(24, 1)
            sleep(0.05)
            led.set_output(24, 0)
            sleep(0.05)
        led.set_output(24,0)
        break
