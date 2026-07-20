"""
ws2812 is also known as "NeoPixel" (Adafruit's name)
The file ws2812.py must reside on the Pico!
"""
import time
import ws2812

strip = ws2812.NeoPixel( brightness=0.1 )

while True:
    strip.pixels_set( 0, strip.RED )
    strip.pixels_show()
    time.sleep(1)
    strip.pixels_set( 1, strip.GREEN )
    strip.pixels_show()
    time.sleep(1)
    strip.pixels_set( 2, strip.BLUE )
    strip.pixels_show()
    time.sleep(1)

    strip.pixels_set( 0, strip.BLACK )
    strip.pixels_set( 1, strip.BLACK )
    strip.pixels_set( 2, strip.BLACK )
    strip.pixels_show()
    time.sleep(1)

# task: make the 3rd Neopixel light up YELLOW
