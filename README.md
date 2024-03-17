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

## Setup
Set up the parts as shown below:
[Wiring diagram](diagram.png) [Picture of breadboard](image.png)

## Packages
On the Raspberry Pi, most modules should be pre-installed with python3:
+ socket
+ tkinter
+ time

You may need to run `[sudo] pip install func_timeout` to install func_timeout. For reference, I'm using version 4.3.5

On the Raspberry Pi Pico W, if not already using MicroPython, you must flash the device with the MicroPython uf2 (go to [MicroPython's website](https://micropython.org/download/RPI_PICO_W/) for more information on how to do this). All necessary modules (machine, utime, socket and network) should already be installed with MicroPython. I'm using MicroPython v1.22.2
