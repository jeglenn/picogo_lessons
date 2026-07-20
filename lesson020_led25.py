import machine
import time

# Onboard LED is connected to GPIO 25
led = machine.Pin(25, machine.Pin.OUT)

delay = 0.5 # seconds

def mytoggle():
    led.toggle()
    time.sleep( delay )
    print( f'the led value is: {led.value()}' )

if __name__=='__main__': 
	# When you run this file on the Pico, __name__=='__main__' is True!
	# when you "import" this file on the Pico, __name__=='__main__' is False

    # if you run this file directly (instead of importing it) then __name__ = '__main__'
    print( "begin" )
    mytoggle() #<-- you call the function with ()
    yourtoggle = mytoggle # but you "point to" a function (without calling it) by leaving out the ()
    
    while True:
        yourtoggle()

        
#
# Task: try making the LED flash at different speeds
#
