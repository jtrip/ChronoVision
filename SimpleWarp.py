import Adafruit_BBIO.ADC as ADC
import mplayer as MP
from time import sleep
from random import randint
from math import floor


def checkKnob(potPin):
    value = ADC.read(potPin)
    return int(floor(5 * value))

def main():
    ADC.setup()
    potPin = 'P9_33'
    running = True

    # setup mplayer
    video = MP.Player()
    video.loadfile('/media/COS_66_F/simple.mov')
    video.fullscreen = True
    video.lopp = 100

    timecode = 1
    videoTimes = [ 254,
                   190,
                   90,
                   77,
                   1]


    while running:
        firstValue = checkKnob(potPin)
        sleep(1)
        secondValue = checkKnob(potPin)
        
        if firstValue != secondValue:
            timecode = videoTimes[checkKnob(potPin)]
            video.time_pos = timecode


if __name__ == "__main__":
    main()
