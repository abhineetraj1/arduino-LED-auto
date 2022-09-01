#Arduino LED width python A.I.
LED blinking with voice command.

Python + Arduino project.
## Installation
1) Download Arduino IDE and python3.x
2) Upload StandardFirmata.ino code in arduino
3) Install python3.X and libraries in requirements.txt

``` pip3 install -r requirements.txt```

4) Run the main.py file
### Note
Make sure that your device is connected with microphone

## Circuit of Arduino

*  Pin 2 = Positive terminal of 1k ohms resistor
*  GND   = Negative terminal of the battery
*  5V    = Positive terminal of the battery
*  LED +ve terminal = Resistor -ve Terminal
*  LED -ve terminal = -ve terminal of battery

## Execution
Say "Turn on" on mic to switch on the LED light and "Turn off" on mic to switch off the LED light.
