# Thonny
- a light-weight text editor
	- text-editors are used for writing code
	- they read the code you write and format it for easy read
- used to write Python code for the Pico
  - raspberry pi 5 (a COMPUTER running Linux) vs pico (A microcontroller running natively python)
  - You need a computer to program a pico!  We're using a laptop running Linux for that.
	- You can use a Windows PC, a Mac, a Linux PC or a chromebook*
		- chromebook needs to run a linux virtual machine in a sand-box (requiring permissions)
		- iPad's do not support Thonny:-(
- Thonny can run Python locally, or on an attached Pi!
- Thonny can write files to your Pi or store them locally
- Let's write a "hello world" script and run it locally
	- File --> New
		- add text:
			print("hello world")
		- Save file as hello.py
	- Click on the lower-right corner of the Thonny window & select "Local Python3"
	- click the green "play" button on the upper menu bar
- now lets attach a pi and run it there.
	- use the USB cord to connect the Pi
	- in Thonny, click on the lower right corner again, but this time select 
		- MicroPython (Raspverry Pi Pico) * /dev/ttyACM0 
		- note: MicroPython (RP2040) * /dev/ttyACM0 should also work, there are just two pointers to the same device
	- notice the "Shell" window shows "MicroPython v1.28.0 on 2026-04-06; Raspberry Pi Pico2 with RP2350"
	- now, press the green "play" button in the upper left of the menu-bar
		- this time hello.py is running on the Pico and the "hello world" text is being passed back via the USB cable!
	- Notice the lower-left corner of the window shows "RP2040 device".  These files listed there are ON the Pico, not the laptop.
		- It looks like of like a USB drive
	- now lets save it to the Pico
		- Under "This Computer" (your laptop) you'll see your file named hello.py.  
			- right-click over hello.py (alt-click)
				- Upload to /
				- this will copy the file to the Pico
			- now double-click on hello.py in the "RP2040 device" window.
				- This opens up the new copy in a new tab in Thonny.  Notice you still have the original copy open in another tab.
			- press the green "play" buggot on the menu-bar.  This is running this new copy.  
				- change the text and re-run it.

	- time for lesson050.py



			- now, lets make sure we have the Pico version's tab open.  Select File->Save As...
				- "RP2040 device"
				- save the file with a new name: "main.py"
					- The file named "main.py" *automatically* runs when the Pico is powered-up

