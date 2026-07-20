"""
Rasperry Pi Pico pin out!

+-------------------------------------------------------------+
| 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1 |
|                                           +---+             |
|                          +-----+          |but|        /----|
|                          | CPU |          +---+        | um |
|                          |     |                       | usb|
|                          +-----+                       \----|
|                                                             |
| 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 |
+-------------------------------------------------------------+

TRSensor.py file must reside on the pico!
PicoGO must be turned on for this to work.
(Right click under lessons --> Upload to / )

Use card with BLACK stripe
"""

import time
import TRSensor
TRS=TRSensor.TRSensor()
import ws2812
strip = ws2812.NeoPixel(brightness=0.01)

WS2TRS = {
    # WSLED number : sensor number 
    3 : 0,
    2 : 1,
    #ignore the middle sensor
    1 : 3,
    0 : 4,
    }

while True:
    TRS_values = TRS.AnalogRead()
    print( TRS_values )
    for num in range( len( WS2TRS ) ): 
        if TRS_values[ WS2TRS[num] ] < 300: # sensor trigger level between 0 and 1000
            strip.pixels_set( num , strip.BLACK )
        else:
            strip.pixels_set( num , strip.RED )
    strip.pixels_show()

    time.sleep(0.1)
