import machine
import time

# Onboard LED is typically on GPIO 25
led = machine.Pin(25, machine.Pin.OUT)

def mytoggle( i ):
  led.toggle()
  time.sleep( 0.1*i )
  print( f'the led value is: {led.value()}' )


# a stand-alone test case for this module
if __name__=='__main__':
    # if you run this file directly (instead of importing it) then __name__ = '__main__'
    
    while True:
        mytoggle( 1 )

