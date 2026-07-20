"""
The Distance Sensor Right and Left [DSR & DLR] are infarred sensors
that 'trip' if an object is closer than some threshold.
There are on-board LEDs labeld LEDR and LEDL on the board, these turn 
one when the respective sensor is tripped (indepented of the software).

On-board potentiometers set the distance where these sensors trip.  A
screwdriver is needed to adjust these.  (I suggest you DO NOT adjust them.)

"""
import utime
from machine import Pin

DSR = Pin(2, Pin.IN) # Potentiometers control sensitiveity
DSL = Pin(3, Pin.IN)

while True:
    DR_status = DSR.value()
    DL_status = DSL.value()

    if((DL_status == 0) and (DR_status == 0)):
        print( 'LEFT RIGHT' )
    elif((DL_status == 0) and (DR_status == 1)):
        print( 'LEFT -----' )
    elif((DL_status == 1) and (DR_status == 0)):
        print( '---- RIGHT' )
    else:
        print( '---- -----' )

    utime.sleep_ms(10)

# Exercise: use the ws2812 (NeoPixels) show if the DSR or DSL trip! 
