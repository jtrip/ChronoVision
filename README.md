# ChronoVision

[![Join the chat at https://gitter.im/jtrip/ChronoVision](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jtrip/ChronoVision?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)  

python tools and arduino module for the:  
**ChronoVision** project at Maker Faire Detroit 2015 from i3Detroit


## Video Display
### BeagleBone Black
_testing with:_ **video_test.py**  
Depends on [mplayer.py](https://github.com/baudm/mplayer.py)  
Create a player, load one file, and control play head position.


## Rotary Encoder and VFD User Interface

### Ardunio
_running:_ **chronovision.ino**   
Depends on an Encoder library, and VFD Library.

### BeagleBone Black 
_testing with:_ **pinCheck_test.py**  
Depends on [Adafruit_BBIO.GPIO](https://github.com/adafruit/Adafruit_Python_GPIO)  
One pin reflects if knob is being moved and so testing for that.  

_testing with:_ **readYear.py**  
Depends on [Adafruit_BBIO.GPIO](https://github.com/adafruit/Adafruit_Python_GPIO)  
An attempt to read the parallel interface the arduino is providing. 
It should be 10 bits for the 'year'.
