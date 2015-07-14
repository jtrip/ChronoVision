import Adafruit_BBIO.GPIO as gpio
from time import sleep


def setup_pin_list():
    pins = []
    base_name = "P8_"
    for x in range(7,20):
        if x < 10:
            pins.append(base_name + '0' + str(x))
        else:
            pins.append(base_name + str(x))

    print(pins)
    return pins


def setPinsGPIOin(pins):
    pinDict = {}
    for pin in pins:
        gpio.setup(pin, gpio.IN)
        pinDict[str(pin)] = str(gpio.input(pin))
    print pinDict


def setupFallDetect(pin):
    try:
        gpio.add_event_detect(pin, gpio.FALLING)
    except:
        print('error')
    print(pin + " : " + str(gpio.input(pin)))


def isMoving(pin):
    return gpio.event_detected(pin)


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


def inv_detectknob(knob):
    running = True
    while running == True:
        if isMoving(knob) != True:
            while gpio.input(knob):
                print('detected')
                sleep(.1)
        else:
            print('checking')
            userInput = raw_input('keep checking?')
            if userInput == 'n':
                running = False
            else:
                running = True
        sleep(.1)


def check_all(pins):
    dict = {}
    for pin in pins:
        dict[pin] = gpio.input(pin)
    print dict




def main():
    knob = 'P8_10'

    pins = setup_pin_list()
    setPinsGPIOin(pins)
    check_all(pins)
    setupFallDetect(knob)


    input = raw_input('check?')
    if input == 'y':
        pass
    else:
        exit()

#   detectKnob(knob)
    inv_detectknob(knob)


if __name__ == "__main__":
    main()
