from time import sleep
import Adafruit_BBIO.GPIO as gpio

knob = 'P8_10'

gpio.setup(knob, gpio.IN)

gpio.add_event_detect(knob, gpio.FALLING)

def run():
    running = True
    while running == True:
         print 'running'
         if gpio.event_detected(knob):
             print 'detected'
             userInput = raw_input('wut?')
             if userInput == 'q':
                 running = False
             else:
                 running = True
         else:
             running = True
             print '.'
             sleep(1)


run()
