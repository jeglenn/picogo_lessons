"""
The UltraSonice sensor has built-in "on-board" functions.
Here we use a burst of eight 40kHz tones and measure how long it takes 
to bounce off of someting and travel back to the the receiver as an echo.

The tone pulses are sent on the FALLING EDGE OF Trig!

To make the sensor send out a pulse, you have to 
send a specific trigger signal.

The Trigger Sequence:

* You set Trig to 1 (High): You must hold it high for at least 10us. 
  During this window, the sensor is simply waiting to make sure it 
  received a valid trigger command. No sound is emitted yet.

* You set Trig to 0 (Low): The falling edge of this signal tells the 
  sensor's internal controller, "Okay, start the measurement now."

* The Chirp Begins: Immediately after Trig goes low, the sensor 
  automatically emits its 8-cycle burst of 40 kHz sound.

* The Echo Pin Goes High: At the exact same moment the sensor finishes 
  sending that sonic chirp, it raises the Echo pin to 1 (High). 

* It keeps Echo high while it waits, and only drops it back to 0 (Low) 
  the instant it hears the returning reflection.

            +--------+
Trig        |        | 10us pulse
____________|        |__________________________________________________

                      |||||||| (8-cycle 40kHz sonic burst emitted)
Sonic Wave            ||||||||
______________________||||||||__________________________________________

                             +-----------------------------------+
Echo                         |                                   |
_____________________________|                                   |______
                             <--------- Time High (dT) --------->
                                      (Sound traveling)

Distance = ( {Speed of Sound} * {Time Echo==1} ) / 2

If the echo pin stays high for 10mu, the total distance traveled by the 
sound is 3.43mm, meaning the object is actually 1.715mm away!
"""

import utime
from machine import Pin

Echo = Pin(15, Pin.IN)
Trig = Pin(14, Pin.OUT)
Trig.value(0)

def dist():
    Trig.value(1)
    utime.sleep_us(10)
    Trig.value(0)
    while(Echo.value() == 0):
        pass
    ts=utime.ticks_us()
    while(Echo.value() == 1):
        pass
    te=utime.ticks_us()
    distance=((te-ts)*0.034)/2
    return distance

while True:
    print("Distance:%6.2f cm" % dist())
    utime.sleep(1)
