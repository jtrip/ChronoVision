import Adafruit_BBIO.GPIO as gpio
from time import sleep
from collections import OrderedDict as od

def setup_pin_list(start, stop):
    pins = []
    pins = ['P9_14', 'P9_16', 'P8_08', 'P8_09', 'P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16', 'P8_17']
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
