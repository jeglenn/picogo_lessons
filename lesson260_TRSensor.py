"""
TRSensor = (line) tracking sensor array

TRSensor.py file must reside on the pico!
PicoGO must be turned on for this to work.
(Right click under lessons --> Upload to / )

Use card with BLACK stripe
"""

import time
import TRSensor

print("\nTRSensor Test Program ...\r\n")
TRS=TRSensor.TRSensor()
while True:
    print(TRS.AnalogRead())
    time.sleep(0.1)

# task:
# add code for the 4 ws2812 (Neopixels) that react to the line 5 tracer sensors 
