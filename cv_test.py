from time import sleep
import mplayer as mp


bg = mp.Player()
fg = mp.Player()
sg = mp.Player()

bg.osdlevel=0

bg.loadfile('videos/test.mpg')
print('bg:' + str(bg.length))

bg.fullscreen=True
bg.loop=20

sleep(5)

fg.loadfile('videos/test2.mpg')
print('fg:' + str(fg.length))

fg.fullscreen=True

sleep(25)

sg.loadfile('videos/test2.mpg')

sleep(30)
