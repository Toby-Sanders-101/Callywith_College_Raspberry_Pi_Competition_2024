# Raspberry Pi Competition - PA Consulting
## Introduction
This app was developed by the team at Callywith College for the PA Raspberry Pi Competition 2024, where the objective was to create software (predominantly using a raspberry pi) that can help someone's health. It is designed to analyse the health of the user using a series of questions, sensors and calculations. The target audience is gamer's as they are a notoriously unhealthy subpopulation. The main software and display is on the Raspberry Pi; a Pico W is used to collect certain data before sending the results to the Pi via a WiFi connection.


## Parts/devices
+ Raspberry Pi with connection to any WLAN (I'm using the Raspberry Pi 3b)
+ Raspberry Pi Pico W(H)
+ Breadboard (or you can solder the parts together)
+ 1 MAX30102 sensor (it must use a V8520 MCU - for example [this one](https://www.dfrobot.com/product-2529.html))
+ 8 Male-to-male wires
+ 2 LEDs (ideally different colours)
+ 1 5V DC power supply (ideally batteries for portability)
+ 1 Momentary push button
+ 1 330&Omega; resistor
+ 1 1k&Omega; resistor
+ 1 USB to microUSB cable


## Packages
On the Raspberry Pi, most modules should be pre-installed with python3:
+ socket
+ tkinter
+ time

You may need to run `[sudo] pip install func_timeout` to install *func_timeout*. For reference, I'm using version 4.3.5

You should also [install Thonny](https://thonny.org) on the Pi

On the Raspberry Pi Pico W, if not already using MicroPython, you must flash the device with the MicroPython uf2 (go to [MicroPython's website](https://micropython.org/download/RPI_PICO_W/) for more information on how to do this). All necessary modules (*machine*, *utime*, *socket* and *network*) should already be installed with MicroPython. I'm using MicroPython v1.22.2


## Setup
1. Turn on the Raspberry Pi and connect to the Internet
2. Download and unzip this repository
3. Set up the parts as shown below:

<img src="diagram.png" width="300" height="400"/> <img src="image.png" width="300" height="400"/>

> [!WARNING]
> Remove the DC power supply at this point because having this connected while the Pico is connected to the computer could damage the electronics

4. If the Pico is already using MicroPython, use the USB-to-microUSB cable to connect the Pico to the Raspberry Pi. Otherwise, [install MicroPython](https://micropython.org/download/RPI_PICO_W/) first
5. Open Thonny and select the Pico (RP2040) as the interpretter
6. Transfer the Pico's code (from this repository) to the Pico
7. Modify lines 14 and 15 in *Pico_W_Code/main.py* so it can connect to your network (this must be the same LAN that the Raspberry Pi is connected to)
8. Run main.py on the Pico. Make a note of the first IP address (of the array of addresses) printed in the Shell
9. Set line 9 in *Raspberry_Pi_Code/socket_client.py* to `pico = socket.getaddrinfo(addr,80)` where *addr* is the string of the Pico's IP address
10. Remove the USB cable and reattach the DC power supply - it is all set up and ready for use now!


## Instruction
1. Connect the DC power supply to the breadboard. After a second or two, you should see the LED at Pin 2 (GP1) light up for two seconds before turning off - this means the *main.py* script is running properly
2. Over the next minute or so, the LED at Pin 4 (GP2) will flash on for one second then turn off again for a few seconds repeatedly until it connects to the WLAN. You will know that it has connected properly because that LED will turn on and stay on until the device loses power or encounters an error
3. Run *Raspberry_Pi_Code/main.py* on the Raspberry Pi. This will open the GUI and attempt to connect to the Pico. As long as the Pico has connected to the same WLAN as the Pi is on, and the Pi is setup to connect to the correct IP address, they will connect and exchange confirmation message to each other
4. Go through the GUI and complete all the sections as accurately as possible (you may need additional measuring devices for some parts)
5. For the **Blood/Temperature** and **Breathing** sections, press the **Get Readings** button. Read the instructions in the pop-up box then close it (by pressing **OK**). This will then alert the Pico that you want to get the correspnoding data. Here is a more detailed descriptions of the details:
   - For the **Blood/Temperature** readings, hold one finger down on the sensor on the MAX30102. There should be a red light under your finger while you do this. Hold it there until either/both the red light turns off or the GUI displays new readings underneath the clicked button; this should take about 10 seconds
   - For the **Breathing** readings, breathe normally but everytime you get to the same point in a breath (eg at the top), press the push button on the breadboard. Do this about 7 times and it will calculate your average breathing rate. You will know that it has finished because the readings in the GUI will update
  
> [!TIP]
> If any of these readings seem drastically wrong, you can redo them as many times as you want!

6. Once all the sections are completed fully, press **Submit**. The computer will process all your data and give you a full analysis of your health including a personalised list of improvements to make
7. Finally you can press **Quit** and it will terminate the connection to the Pico then close the GUI
8. If you want to do it again, reopen *Raspberry_Pi_Code/main.py* and it should reconnect to the Pico
9. To turn off or restart the Pico, simply remove the power source (and reattach it to reset it)

## Explanation
+ Raspberry_Pi_Code
  + gui.py
    + MyEntry (class)
      
      This is a simple derived class (inheriting methods and properties from the tkinter.Entry class) with a few extra methods: for each mode (string, integer only, float only) there is one method (eg makeInt()) to set the instance as one of these modes, and another method (eg validateInt) that validates the input everytime the value of the object changes.
    + GUI (class)
  + main.py
  + socket_client.py 
+ Pico_W_Code
