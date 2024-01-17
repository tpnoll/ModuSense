import time
import machine
import pins
import helper
from machine import Pin, PWM, time_pulse_us
import utime

# The distance in cm at which to blow air
compress_distance = 4

# Define GPIO pins
trigger_pin = Pin(8, Pin.OUT)
echo_pin = Pin(9, Pin.IN)

# Send a 10µs pulse to trigger pin
def send_trigger_pulse(pin):
    pin.low()
    utime.sleep_us(2)
    pin.high()
    utime.sleep_us(10)
    pin.low()

# Measure the duration of the echo pulse
def wait_for_echo(value, timeout):
    count = timeout
    while echo_pin.value() != value and count > 0:
        count -= 1
    return timeout - count

# Calculate distance from duration of echo pulse
def distance_in_cm():
    send_trigger_pulse(trigger_pin)
    duration = time_pulse_us(echo_pin, 1, 1000000)
    distance = (duration / 2) * 0.0343
    return distance
    
def run_toy():
    print("Start toy code")
    
    # Flag variable to control state of servo
    is_compressed = 0

    # Print distance in cm
    while True:
        this_distance = distance_in_cm()
        
        print("Distance: %.1f cm" % this_distance)

        # If the servo is not compressed and the kid is within range, compress
        if((this_distance < compress_distance) and (is_compressed == 0)):
            print("Turn the servo to compress")
            is_compressed = 1
            helper.blink_board(2, 0.7)
            helper.drive_servo(0, 90)
                
        # If the servo is compressed and the kid is out of range, decompress
        if((is_compressed == 1) and (this_distance >= compress_distance)):
            print("Turn the servo to de-compress")
            is_compressed = 0
            helper.blink_board(3, 0.5)
            helper.drive_servo(90, 0)
                
        utime.sleep(1)
        



