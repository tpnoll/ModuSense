import time
import machine
from machine import Pin
import pins
import helper

# Main function, called by init.py
def run_toy():
    # Define the button pin 
    input_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
    
    press_count = 0
    
    # Initalize the start time
    start_time = time.time()
    
    # Run forever
    while(True):   
        
        # If the button is pressed (input_pin is logic 1)
        if(input_pin.value()):
            time.sleep(0.1)
            if(input_pin.value()):
                print("Button press detected: ", press_count)
                press_count = press_count + 1
                time.sleep(0.3) # Debounce
        
        # Check if enough seconds have passed to start a vibration
        end_time = time.time()
        if(end_time - start_time > 2):
            print("Check press count")
            
            if(press_count == 1):
                play_vibration(1, input_pin)
            elif(press_count == 2):
                play_vibration(2, input_pin)
            elif(press_count > 3):
                play_vibration(3, input_pin)
                
            # Reset the vibration counter
            press_count = 0
            start_time = time.time()

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




