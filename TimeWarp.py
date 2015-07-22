import Adafruit_BBIO.GPIO as GPIO
import mplayer as mp
from time import sleep
from random import randint


def knobTime():
    return 1 # needs to be replaced by time data GPIO or Serial

def checkKnob():
    return randint(0,1) # needs to be replaced by GPIO data

def main():
    print('start')

    running = True


    # Setup GPIO 
    knobReading = 0
    knobMoving = False
    
    # Setup mplayer
    video = mp.Player()
    video.loadfile('/home/debian/videos/test.mpg')
    video.fullscreen = True
    
    timecode = 1 #do not use zero, it creates a pause
    
    # time in seconds, where there is static I want to use
    staticStart = [1,7,10,14,20]
    staticLength = [3,4,10,7,9] # corresponding length of each static clip
    
    # outter most loop, keep service running
    while running:
        
        # just play
        
        # respond to input
        while knobMoving == True:
            knobChoice = randint(0,4) # so I can use this to correlate staticStart and staticLength
            video.time_pos = staticStart[knobChoice]
            print(video.time_pos)
            sleep(1)
            knobMoving = checkKnob()
            if knobMoving == False:
                video.time_pos = knobTime() 
                break
            someTime = randint(2,staticLength[knobChoice])
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
    
    print('end')

if __name__ == "__main__":
    main()