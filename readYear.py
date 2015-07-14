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


def check_all(pins):
    pinDict = od()
    for pin in pins:
        pinDict[pin] = gpio.input(pin)
    print pinDict


def checkCycle(pins):
    count = 0
    pinDict = od()
    running = True
    while running == True:
        for pin in pins:
            pinDict[pin] = gpio.input(pin)
        #print pinDict
        values = []
        for pin,value in pinDict.items():
            values.append(pinDict[pin])
        reverse_values = values[::-1]
        if count%2 == 0:
            print('L->H' + str(values) + " = " + str(int(''.join(str(int(value)) for value in values), 2)))
            #print('H->L' + str(reverse_values) + " = " + str(int(''.join(str(int(value)) for value in reverse_values), 2)))

        count += 1
        if count%2 == 0:
            userInput = raw_input('continue?')
            if userInput == 'n':
                running = False
            else:
                running = True



def main():

    pins = setup_pin_list(8,18)
    setPinsGPIOin(pins)

    input = raw_input('check?')
    if input == 'y':
        pass
    else:
        exit()

    checkCycle(pins)




if __name__ == "__main__":
    main()
