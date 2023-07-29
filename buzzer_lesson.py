import machine
import time

p23=machine.Pin(23,machine.Pin.OUT)

buzzer=machine.PWM(p23)

buzzer.freq(1047)
buzzer.duty(50)

time.sleep(1)

buzzer.duty(0)
buzzer.deinit()