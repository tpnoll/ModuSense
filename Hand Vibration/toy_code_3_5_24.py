import time
import machine
from machine import Pin
import pins

# Runs when an interrupt occurs
def callback(pin):
    global interrupt_flag
    global vibration_selection
    interrupt_flag = 1
    vibration_selection = vibration_selection + 1
    
    print("Interrupt Recieved")
    if(vibration_selection > 3):
        vibration_selection = 1

def run_toy():
    global interrupt_flag
    global vibration_selection
    interrupt_flag = 0
    vibration_selection = 1
    
    # Define the button pin and enable interrupts
    input_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
    input_pin.irq(trigger=Pin.IRQ_RISING, handler=callback)
    
    # Run forever
    while(True):
        # If an interrupt is recieved
        if(interrupt_flag == 1):
            print("Interrupt detected, calling play_vibration: ", vibration_selection)
            play_vibration(vibration_selection, input_pin)
            interrupt_flag = 0

# Play vibration pattern until button is released 
def play_vibration(vibration_selection, input_pin):
    output_pin = machine.Pin(16, machine.Pin.OUT)
    n = 0
    while(input_pin.value() == 1):
        print(n)
        n = n + 1
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




