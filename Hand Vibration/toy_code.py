import time
from time import ticks_diff
import machine
import pins
import helper

# Initialize counter and last press time
button_press_count = 0
last_press_time = ticks_ms()

def button_handler(pin):
    global button_press_count
    global last_press_time
    
    current_time = ticks_ms()
    
    print("Button Press!")
    helper.blink_board(1, 0.5)
    
    # Button debounce of Xms
    if(current_time - last_press_time >= 50):
        last_press_time = current_time
        button_press_count = button_press_count + 1
        if(button_press_count > 3):
            button_press_count = 1
        
def run_toy():
    global button_press_count
    global last_press_time
    
    # Define input pin for the button 
    input_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
                            
    # Attach interrupt handler to the input pin
    input_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

    output_pin = machine.Pin(16, machine.Pin.OUT)
    
    # Loop forever
    while True:
        while(input_pin.value() == 1):
            if(button_press_count == 1):
                print("Play vibration 1")
                output_pin.high()
                time.sleep(4)
                output_pin.low()
            elif(button_press_count == 2):
                print("Play vibration 2")
                output_pin.high()
                time.sleep(1)
                output_pin.low()
                time.sleep(1)
                output_pin.high()
                time.sleep(1)
                output_pin.low()
            elif(button_press_count == 3):
                print("Play vibration 3")
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
                output_pin.high()
                time.sleep(0.2)
                output_pin.low()
                time.sleep(0.2)
            time.sleep(0.1)




