import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import mplayer as mp
from time import sleep
from random import randint
from math import floor


def checkKnob(potPin):
    # LOL return randint(0,1) # needs to be replaced by GPIO data
    value = ADC.read(potPin)
    return floor(24 * value)

def main():
    print('start')
    potPin = "P9_33"
    running = True


    # Setup GPIO 
    knobReading = 0
    knobMoving = False
    
    # Setup mplayer
    video = mp.Player()
    video.loadfile('/home/debian/videos/test.mpg')
    video.fullscreen = True
    video.loop = 10  # arbitrarily 'large'
    
    timecode = 1 #do not use zero, it creates a pause
    
    # time in seconds, where there is static I want to use
    staticStart = [1,70,100,140,200]
    staticLength = [10,10,9,9,9] # corresponding length of each static clip
    
    # outter most loop, keep service running
    while running:
        
        # just play
        
        # respond to input
        knobMoving = checkKnob()
        while knobMoving == True:
            knobChoice = randint(0,4) # so I can use this to correlate staticStart and staticLength
            video.time_pos = staticStart[knobChoice]
            print(video.time_pos)
            sleep(1)
            knobMoving = checkKnob()
            if knobMoving == False:
                video.time_pos = knobTime() 
                break
            someTime = randint(2,staticLength[knobChoice]-1)
            sleep(someTime)
            knobMoving = checkKnob()
            if knobMoving == False:
                video.time_pos = knobTime() 
    
    
        # only here for testing, otherwise loop forever  
        keepRunning = raw_input('Shall we continue?')
        if keepRunning == 'n':
            running = False
        elif keepRunning == 't':
            knobMoving = True
    
        sleep(0.25)
    
    print('end')

if __name__ == "__main__":
    main()
