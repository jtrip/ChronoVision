import Adafruit_BBIO.GPIO as gpio
from time import sleep
from collections import OrderedDict as od

def setup_pin_list(start, stop):
    pins = []
    base_name = "P8_"
    for x in range(start, stop):
        if x < 10:
            pins.append(base_name + '0' + str(x))
        else:
            pins.append(base_name + str(x))

    print(pins)
    return pins


def setPinsGPIOin(pins):
    pinDict = od()
    for pin in pins:
        gpio.setup(pin, gpio.IN)
        pinDict[str(pin)] = str(gpio.input(pin))
    print pinDict


def setupFallDetect(knob):
    try:
        gpio.add_event_detect(knob, gpio.FALLING)
    except:
        print('error')
    print(knob + " : " + str(gpio.input(knob)))


def isMoving(knob):
    return gpio.event_detected(knob)


def check_all(pins):
    pinDict = od()
    for pin in pins:
        pinDict[pin] = gpio.input(pin)
    print(pinDict)


def detectKnob(knob):
    running = True
    while running == True:
        if isMoving(knob) == True:
            print('detected')
            userInput = raw_input('keep checking?')
	    if userInput == 'n':
                running = False
            else:
                running = True
        else:
            print('checking...')
        sleep(.1)




def main():
    knob = 'P8_07'

    pins = setup_pin_list(7,20)
    setPinsGPIOin(pins)
    check_all(pins)

    setupFallDetect(knob)


    input = raw_input('check?')
    if input == 'y':
        pass
    else:
        exit()

    detectKnob(knob)


if __name__ == "__main__":
    main()
