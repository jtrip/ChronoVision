from Adafruit_BBIO import ADC
from math import floor

def checkPot(potPin):
    value = ADC.read(potPin)
    print(value)
    print (24 * value)
    return floor(24 * value)

def main():
    ADC.setup()
    potPin = "P9_33"
    running = True

    while running == True:
        print('first check')
        print(checkPot(potPin))
        print('second check')
        print(checkPot(potPin))
        
        user_input = raw_input('check again?')
        if user_input == 'n':
            running = False



if __name__ == "__main__":
    main()
