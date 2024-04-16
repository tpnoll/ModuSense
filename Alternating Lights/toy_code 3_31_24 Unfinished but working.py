import time
import machine
from machine import Pin
import pins
import helper

# Main function, called by init.py
def run_toy():
    # Define the button pin 
    input_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
    
    # Run forever
    while(True):
        #print(input_pin.value())
        
        # If the button is pressed (input_pin is logic 1)
        if(input_pin.value()):
            # Button debounce, make sure the signal persists
            time.sleep(0.1)
            if(input_pin.value()):
                print("Button press detected!")
                play_vibration(1, input_pin)
                time.sleep(1) # Debounce

# Play vibration pattern until button is released 
def play_vibration(vibration_selection, input_pin):
    output_pin = machine.Pin(16, machine.Pin.OUT)
    
    helper.blink_board(1,1)
    
    while(input_pin.value() == 1):
        if(vibration_selection == 1):
            print("Play vibration 1")
            output_pin.high()
            time.sleep(4)
            output_pin.low()
        elif(vibration_selection == 2):
            print("Play vibration 2")
            output_pin.high()
            time.sleep(1)
            output_pin.low()
            time.sleep(1)
            output_pin.high()
            time.sleep(1)
            output_pin.low()
        elif(vibration_selection >= 3):
            print("Play vibration 3")
            for i in range(5):
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
        time.sleep(0.1)




