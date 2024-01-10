import machine
import time
import pins

# Blink the on board LED for time_duration num_blink times
def blink_board(num_blink, time_duration):
    pin = machine.Pin(pins.BOARD_LED, machine.Pin.OUT)
    for i in range(num_blink):  
        pin.high()
        time.sleep(time_duration)
        pin.low()
        time.sleep(time_duration)
        
# Set a servo position to the specified angle
def drive_servo(servo_angle):
    # Prevent illegal angles
    if((servo_angle > 0) and (servo_angle < 180)):
        # Initalize designated servo pin to drive PWM
        pin = machine.PWM(pins.SERVO_PIN_1, freq=50)

        # Define a duty cycle to pass through the pin to the servo
        instruction = int(500 + ((servo_angle * 2000) / 180))
        pin.duty_u16(instruction)
