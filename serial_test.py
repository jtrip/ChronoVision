import Adafruit_BBIO.UART as uart
import serial

uart.setup('UART1')

ser = serial.Serial(port="/dev/tty01",baudrate=9600)
ser.close()
ser.open()

if ser.isOpen():
    print "Serial is Open"
    ser.write("Heyo!")
ser.close()



#uart.cleanup()