# ModuSense Initialization Program

# Python Libraries
import machine
import time

# Import helper functions and toy specific code
import helper
import toy_code

# Called by boot.py
def on_board_start():
    # Detect if microcontroller is connected to a computer
    if machine.UART(0).any():
        helper.blink_board(2, 1)
        time.sleep(5)
        
        # If it is, enter debug mode
        debug_mode()
        
    # Otherwise run the toy code
    else:
        helper.blink_board(3, 1)
        
        time.sleep(5)
        
        toy_code.run_toy()
        
def debug_mode():
        toy_code.run_toy()
        
        print("Debug Mode: Exiting to UART")
        
        

