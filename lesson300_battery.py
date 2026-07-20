"""

"""
from machine import Pin
import utime

bat = machine.ADC(Pin(26)) # Analog 2 Digital Converter

v = bat.read_u16()*3.3/65535 * 2
print( f"V(battery)={v}" )
