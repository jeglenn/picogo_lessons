"""
Rasperry Pi Pico pin out!

+-------------------------------------------------------------+
| 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1 |
|                                           +---+             |
|                          +-----+          |but|        /----|
|    PICO                  | CPU |          +---+        | um |
|                          |     |                       | usb|
|                          +-----+                       \----|
|                                                             |
| 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 |
+-------------------------------------------------------------+
        self.rst = Pin(12,Pin.OUT)
        self.bl = Pin(13,Pin.OUT
        self.cs = Pin(9,Pin.OUT)
        self.spi = SPI(1,10000_000,polarity=0, phase=0,sck=Pin(10),mosi=Pin(11),miso=None)
        self.dc = Pin(8,Pin.OUT)

+-----------------------------------------------------------------------
| PicoGo Pin Assignments...
+------------------+--------+--------------------------------
|                  | Pico   |                    
| Component        | CODE   | Example            
|                  | NAME   |                    
+------------------+--------+--------------------------------
| IR Sensor Right  | gpio2  | lesson080_IR2_IR3.py
| IR Sensor Left   | gpio3  | lesson080_IR2_IR3.py
| Motor Left PWM   | gpio16 | lesson090_motor.py
| Motor Left IN+   | gpio17 | lesson090_motor.py
| Motor Left IN-   | gpio18 | lesson090_motor.py
| Motor Right IN-  | gpio19 | lesson090_motor.py
| Motor Right IN+  | gpio20 | lesson090_motor.py
| Motor Right PWM  | gpio21 | lesson090_motor.py
| LCD Chip Select  | gpio9  |
| LCD Serial Clock)| gpio10 |
| LCD Data (mosi)  | gpio11 |
| LCD Reset        | gpio12 |
| LCD BackLight    | gpio13 |
| Ultrasonic TRIG  | gpio14 | lesson100_Ultrasonic.py
| Ultrasonic ECHO  | gpio15 | lesson100_Ultrasonic.py
| "NeoPixels" LEDs | gpio22 | lesson050_ws2812.py
| LED on Pico Board| gpio25 | lesson020_led25.py
| Battery Voltage  | gpio26 | lesson300_battery.py
| LineTrack SPI CLK| gpio6  | lesson260_TRSensor.py
| LineTrack SPI ADD| gpio7  | lesson260_TRSensor.py
| LineTrack SPI DAT| gpio27 | lesson260_TRSensor.py
| LineTrack SPI CS | gpio28 | lesson260_TRSensor.py
| IR Receiver      | gpio14 |

+------------------+--------+--------------------------------
"""
