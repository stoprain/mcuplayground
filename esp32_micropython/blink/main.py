import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
but = machine.Pin(0, machine.Pin.IN)

while True:
    but_status = but.value()
    if but_status == False:
        led.value(1)
    else:
        led.value(0)