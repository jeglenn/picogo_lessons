"""
ST7789.py must reside on the Pico!

These colors are in 4-digit hex code (weird).  So 
Red: 5 bits
Green: 6 bits
Blue: 5 bits

Then, on top of that, the bit orders are swapped to
make the hexidecial.  The color565 function re-arranges
the order to match our RGB led names

"""
import ST7789
        
def color565(r, g, b):
    # 1. Standard RGB888 to RGB565 packing
    color = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
    
    # 2. Endianness swap: Put low byte first, high byte second
    return ((color & 0x00FF) << 8) | ((color & 0xFF00) >> 8)

LCD_WHITE = color565( 255, 255, 255 )
LCD_RED   = color565( 255,   0,   0 )
LCD_GREEN = color565(   0, 255,   0 )
LCD_BLUE  = color565(   0,   0, 255 )
LCD_BLACK = color565(   0,   0,   0 )  
        
lcd = ST7789.ST7789()

bg = LCD_WHITE
print( f'background hex:{bg:#x}')
lcd.fill(bg) # back-ground

lcd.text( f'screen size x={lcd.width} y={lcd.height}',10,5,LCD_BLACK )

       
lcd.text("Raspberry Pi Pico",10,15, LCD_GREEN) # string,(x,y) location, color
lcd.text("PicoGo",10,25)

# Syntax: lcd.fill_rect(x, y, width, height, color)
lcd.fill_rect(50, 50, 100, 50, LCD_RED)

# Syntax: lcd.rect(x, y, width, height, color)
lcd.rect(70, 75, 100, 50, LCD_BLUE)

# Syntax: lcd.line(x0, y0, x1, y1, color)
lcd.line(0, 0, 240, 135, LCD_RED)

# Syntax: lcd.hline(x0, y, x1, color )
lcd.hline(30, 80, 225, LCD_BLACK)

# Syntax: lcd.vline(x, y0, y1, color )
lcd.vline(20, 70, 130, LCD_RED )

# Syntax: lcd.pixel( x, y, color )
lcd.pixel(10, 35, LCD_BLUE) # hard to see a single pixel!

lcd.show() # if you don't do this, nothing will happen!
    
   

