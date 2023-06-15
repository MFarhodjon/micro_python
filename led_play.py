import machine
import time
led=machine.Pin(2,machine.Pin.OUT)
def led_play(count,time_between):
    i=0
    while i<count:
        led.on()
        time.sleep(time_between)
        led.off()
        time.sleep(time_between)
        i+=1


