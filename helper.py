import machine
import time
import pins
from machine import Pin, PWM # For servo motor
from machine import time_pulse_us

servo = PWM(pins.SERVO_PIN_1)
servo.freq(50)

# Blink the on board LED for time_duration num_blink times
def blink_board(num_blink, time_duration):
    pin = machine.Pin(pins.BOARD_LED, machine.Pin.OUT)
    for i in range(num_blink):  
        pin.high()
        time.sleep(time_duration)
        pin.low()
        time.sleep(time_duration)
        
# Set a servo position to the specified angle
def drive_servo(start_angle, end_angle):
    print("Turn servo")
    for duty in range(start_angle, end_angle, 1):
        servo.duty_u16(duty * 100)
        time.sleep_ms(10)
    
