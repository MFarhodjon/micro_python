import machine
import time

p23=machine.Pin(23,machine.Pin.OUT)

def play(pin,melodies,delays,duty):
    pwm=machine.PWM(pin)
    for note in melodies:
        pwm.freq(note)
        pwm.duty(duty)
        time.sleep(delays)
    pwm.duty(0)
    pwm.deinit()