"""
Simple PicoGo Demo
"""
import time, utime
import ws2812
import machine

led = machine.Pin(25, machine.Pin.OUT) # onboard LED

bat = machine.ADC(machine.Pin(26)) # Battery Sensor Analog 2 Digital Converter

DSR = machine.Pin(2, machine.Pin.IN) # Distance Sensor Right/Left
DSL = machine.Pin(3, machine.Pin.IN)

US_Echo = machine.Pin(15, machine.Pin.IN) # Ultra Sonice Sensor
US_Trig = machine.Pin(14, machine.Pin.OUT)
US_Trig.value(0)

import ST7789
lcd = ST7789.ST7789()

import Motor
M = Motor.PicoGo()

strip = ws2812.NeoPixel( brightness=0.1 )

def led_toggle():
    led.toggle()
    value = led.value()
    print( f'the led value is: {value}' )
    return value

def check_DS():
    '''Check Distance Sensors'''

    DR_status = DSR.value()
    DL_status = DSL.value()

    state = '---- -----'
    if  ((DL_status == 0) and (DR_status == 0)):
        state = 'LEFT RIGHT'
    elif((DL_status == 0) and (DR_status == 1)):
        state = 'LEFT -----'
    elif((DL_status == 1) and (DR_status == 0)):
        state = '---- RIGHT'

    print(f'LR status: {state}')
    return state

def bat_voltage():
    v=bat.read_u16()*3.3/65535 * 2
    print( f"V(battery)={v}" )
    return v

def check_usdist():
    '''check ultra-sonic distance'''
    US_Trig.value(1)
    utime.sleep_us(10)
    US_Trig.value(0)
    while(US_Echo.value() == 0):
        pass
    ts=utime.ticks_us()
    while(US_Echo.value() == 1):
        pass
    te=utime.ticks_us()
    distance=((te-ts)*0.034)/2
    print("Distance:%6.2f cm" % distance)
    return distance

def update_neopixels( _state = [0] ):
    counter = _state[0]

    if _state[0] == 0:
        strip.pixels_set( 0, strip.YELLOW )
    elif _state[0] == 1:
        strip.pixels_set( 1, strip.BLUE )
    elif _state[0] == 2:
        strip.pixels_set( 2, strip.GREEN )
    else:
        strip.pixels_set( 3, strip.RED )
        strip.pixels_set( 2, strip.RED )
        strip.pixels_set( 1, strip.RED )
        strip.pixels_set( 0, strip.RED )
        _state[0] = -1
    _state[0] += 1

    return _state[0]

def color565(r, g, b):
    # 1. Standard RGB888 to RGB565 packing
    color = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)    
    # 2. Endianness swap: Put low byte first, high byte second
    return ((color & 0x00FF) << 8) | ((color & 0xFF00) >> 8)
LCD_WHITE = color565( 255, 255, 255 )
LCD_RED   = color565( 255,   0,   0 )
LCD_GREEN = color565(   0, 255,   0 )
LCD_BLUE  = color565(   0,   0, 255 )
LCD_YELLOW= color565( 255, 255,   0 )
LCD_BLACK = color565(   0,   0,   0 ) 
lcd_bg = LCD_WHITE

def update_screen(led, volts, ds, us, neo, motor):
    '''240x135'''
    lcd.fill(lcd_bg) # back-ground

    lcd.text( f'Room-a-zoom-zoom', 10, 5, LCD_BLACK ) # text y=~15pixels with space
    lcd.hline( 0, 15, 240, LCD_BLACK) # x0, y, x1, color
    
    lcd.text( f'led state: {led}', 10, 20 )
    #lcd.line( 0, 30, 240, 30, LCD_RED) # x0, y0, x1, y1, color

    lcd.fill_rect( 0, 35, 240, 20, LCD_RED) #x, y, width, height, color
    lcd.text( f'v(battery)={volts}V', 10, 40, LCD_WHITE )

    lcd.rect( 0, 55, 240, 20, LCD_BLUE) # x, y, width, height, color
    lcd.text( f'Infarred Dist:{ds}', 10, 60, LCD_BLACK )
    
    lcd.text( f'UltraSonic:{us}cm', 10, 80 )

    lcd.fill_rect( 0, 90, 240, 20, LCD_YELLOW) #x, y, width, height, color
    lcd.text( f'NeoPixel state:{neo}', 10, 95, LCD_RED )
    
    lcd.text( f'Motor State: {motor}', 10, 115, LCD_BLUE )
    #lcd.vline(20, 70, 130, LCD_RED ) # x, y0, y1, color
    #lcd.pixel(10, 35, LCD_BLUE) #  x, y, color

    lcd.show()

def update_visuals( move ):
    led_state = led_toggle()
    voltage = bat_voltage()
    ds_state = check_DS() # l/r sensors
    us_state = check_usdist() # ultrasonic dist
    
    neo_state = update_neopixels()
    
    update_screen( led_state, voltage, ds_state, us_state, neo_state, move )

def update_motors( move ):
    if move == 'stop':
        # The stop method doesn't take a speed argument
        M.stop()
    else:
        # 1. Grab the function dynamically using its string name
        motor_function = getattr(M, move)
        # 2. Execute the function and pass the speed (0 to 100)
        motor_function(10)
        utime.sleep(0.5)
        
for move in ['forward','left','right','backward','stop']:
    update_motors( move )
    update_visuals( move )
