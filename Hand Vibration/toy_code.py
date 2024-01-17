import time
import machine
import pins

def run_toy():
    print("Running toy code")
    
    input_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # Count how many times the button has been pressed in a one second interval 
    button_press_count = 0

    # Boolean is the button currently being pressed
    button_is_pressed = 0

    # Take the current time
    timer_start = time.time()

    # Loop forever
    while True:
        if (input_pin.value() == 0) and (button_is_pressed == 0):
            print("Press " + str(time.time()))
            print(button_press_count)
            time.sleep(0.1)
            #print("Button was pressed!")
            button_press_count = button_press_count + 1
            button_is_pressed = 1
        elif(input_pin.value() != 0):
            button_is_pressed = 0
            
        # Every second interpret any button presses
        if(time.time() - timer_start >= 1):
            if(button_press_count > 0):
                play_vibration(button_press_count, input_pin)
            button_press_count = 0
            timer_start = time.time()

# Play vibration pattern until button is released 
def play_vibration(vibration_selection, input_pin):
    output_pin = machine.Pin(20, machine.Pin.OUT)
    while(input_pin.value() == 0):
        print(vibration_selection)
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




