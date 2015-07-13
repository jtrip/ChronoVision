from time import sleep
import mplayer as mp


bg = mp.Player()

bg.osdlevel = 0
bg.loadfile('videos/test.mpg')
bg.fullscreen=True

bg.loop=20

sleep(5)

while True:
    userInput = raw_input('when?')
    if userInput == '':
	userInput = 0
    else:
	userInput = float(userInput)
 
    bg.time_pos=userInput

