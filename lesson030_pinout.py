"""
Rasperry Pi Pico pin out!

+-------------------------------------------------------------+
| 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1 |
|                                           +---+             |
|                          +-----+          |but|        /----|
|                          | CPU |          +---+        | um |
|                          |     |                       | usb|
|                          +-----+                       \----|
|                                                             |
| 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 |
+-------------------------------------------------------------+

The Pico Pin numbers do not match the RP2040 (RP2350)
General Purpose Input/Output [GPIO] python virtual machine numbers!

When we write code for the Pico, we need to use this mapping.
+----------+-------------+   +----------+-----------------------+
| Physical | RP2040 GPIO |   | Physical | RP2040 GPIO           |
|    Pin   |  Function   |   |    Pin   |  Function             |
+----------+-------------+   +----------+-----------------------+
| 1        | gpio0       |   | 40       | VBUS (5V USB)         |
| 2        | gpio1       |   | 39       | VSYS (1.8V-5.5V input)|
| 3        | GND         |   | 38       | GND                   |
| 4        | gpio2       |   | 37       | 3V3_EN (Regulator En) |
| 5        | gpio3       |   | 36       | 3V3 (3.3V Output)     |
| 6        | gpio4       |   | 35       | ADC_VREF (ADC Ref)    |
| 7        | gpio5       |   | 34       | gpio28 / ADC2         |
| 8        | GND         |   | 33       | GND / AGND (Analog)   |
| 9        | gpio6       |   | 32       | gpio27 / ADC1         |
| 10       | gpio7       |   | 31       | gpio26 / ADC0         |
| 11       | gpio8       |   | 30       | RUN (Reset pin)       |
| 12       | gpio9       |   | 29       | gpio22                |
| 13       | GND         |   | 28       | GND                   |
| 14       | gpio10      |   | 27       | gpio21                |
| 15       | gpio11      |   | 26       | gpio20                |
| 16       | gpio12      |   | 25       | gpio19                |
| 17       | gpio13      |   | 24       | gpio18                |
| 18       | GND         |   | 23       | GND                   |
| 19       | gpio14      |   | 22       | gpio17                |
| 20       | gpio15      |   | 21       | gpio16                |
+----------+-------------+   +----------+-----------------------+
NOTE: gpio25 (the LED pin) is not actually PINNED-OUT on the Pico!!

"""
put a meter on pin25!  (oh, but it's goota be mapped)
