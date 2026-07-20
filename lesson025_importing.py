import lesson020_led25 # imported file lesson020_led25.py must reside the Pico or be 'built-in' 

lesson020_led25.mytoggle()  # must 'fully qualify' mytoggle() location
lesson020_led25.mytoggle()
lesson020_led25.mytoggle()

from lesson020_led25 import mytoggle # this way I do not have to type lessone020_led25. every time I call mytoggle

while True:
        mytoggle()