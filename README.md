# Arduino LED width python A.I.
This project involves blinking of LED throught Voice command. The code interpretes your voice to text and find the keyword to trigger the function of blinking light.

## Installation
1) Download Arduino IDE and python3.x
2) Upload StandardFirmata.ino code in arduino
3) Install python3.X and libraries in requirements.txt
```
pip3 install -r requirements.txt
```
4) If your facing problem while installing PyAudio in python, then download PyAudio from [here](https://www.lfd.uci.edu/%7Egohlke/pythonlibs/), according to your system configuration and run:-
```
pip3 install filename
```
5) Run the main.py file
### Note :-
Make sure that your device is connected with microphone and internet

## Features
* Automatically connects to arduino through COM, no need to configure COM ports
* Voice command
* User friendly GUI assistant to connect device

## Circuit of Arduino

| Arduino pin | Electronic device |
| --- |:----------: |
| Pin 2 | Positive terminal of 1k ohms resistor |
| GND   | Negative terminal of the battery |
| 5V    | Positive terminal of the battery |
| LED +ve terminal | Resistor -ve Terminal |
| LED -ve terminal | -ve terminal of battery |

## Execution
*  Connect your device to internet.
*  Make sure your microphone is well connected to your device
*  Run app.py file
```
python3 /path/to/folder/main.py
```
* Say "Turn on" on mic to switch on the LED light and "Turn off" on mic to switch off the LED light.

## Programming languages used
<a href="https://www.arduino.cc/" target="_blank" rel="noreferrer"> <img src="https://cdn.arduino.cc/header-footer/prod/assets/favicon-arduino/favicon.ico" alt="blender" width="40" height="40"/> </a><a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>


## Developer
*	[abhineetraj1](http://github.com/abhineetraj1)
