import time
import machine
import pins

def run_toy():
 print("Running toy code")

 input_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
 output_pin = machine.Pin(0, machine.Pin.OUT)  # Use pin0 for output

 while True:
   if input_pin.value() == 0:  # Button is pressed
     output_pin.high()  # Turn on pin0
     time.sleep(4)  # Wait for 4 seconds
     output_pin.low()  # Turn off pin0
     time.sleep(0.5)  # Add a slight delay to prevent multiple triggers

run_toy()