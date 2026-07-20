"""
Motor.py must reside on the Pico!
"""

import Motor
import utime

M = Motor.PicoGo()

M.forward(8) # speed from 8 to 100
utime.sleep(1)
M.backward(100)
utime.sleep(0.5)
M.left(30)
utime.sleep(0.5)
M.right(30)
utime.sleep(0.5)
M.stop()

