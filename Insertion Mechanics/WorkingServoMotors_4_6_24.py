from mfrc522 import MFRC522
import utime
import helper
from machine import Pin, PWM # For servo motor
from machine import time_pulse_us
import time
import machine
 
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

print("Bring TAG closer...")
print("")
 
# The servo motor GPIO pins are: 16-21

# Initialize all of the servos
s1 = PWM(16)
s2 = PWM(17)
s3 = PWM(18)
s4 = PWM(19)
s5 = PWM(20)
s6 = PWM(21)

s1.freq(50)
s2.freq(50)
s3.freq(50)
s4.freq(50)
s5.freq(50)
s6.freq(50)
 
# Establish the start and end angle
start_angle = 5
end_angle = 45
 
 
# Wait for RFID
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
            #helper.blink_board(1,1)
            
            # Turn servo motor 1
            for duty in range(start_angle, end_angle, 1):
                s1.duty_u16(duty * 100)
                time.sleep_ms(10)
                
            # Turn servo motor 2
            for duty in range(start_angle, end_angle, 1):
                s2.duty_u16(duty * 100)
                time.sleep_ms(10)
                
            # Turn servo motor 3
            for duty in range(start_angle, end_angle, 1):
                s3.duty_u16(duty * 100)
                time.sleep_ms(10)
                
            # Turn servo motor 4
            for duty in range(start_angle, end_angle, 1):
                s4.duty_u16(duty * 100)
                time.sleep_ms(10)
                
            # Turn servo motor 5
            for duty in range(start_angle, end_angle, 1):
                s5.duty_u16(duty * 100)
                time.sleep_ms(10)
                
            # Turn servo motor 6
            for duty in range(start_angle, end_angle, 1):
                s6.duty_u16(duty * 100)
                time.sleep_ms(10)

            # Wait to reset motors
            time.sleep(5)
            
            for duty in range(end_angle, start_angle, -1):
                s6.duty_u16(duty * 100)
                time.sleep_ms(10)
            
            for duty in range(end_angle, start_angle, -1):
                s5.duty_u16(duty * 100)
                time.sleep_ms(10)
            
            for duty in range(end_angle, start_angle, -1):
                s4.duty_u16(duty * 100)
                time.sleep_ms(10)
            
            for duty in range(end_angle, start_angle, -1):
                s3.duty_u16(duty * 100)
                time.sleep_ms(10)
            
            for duty in range(end_angle, start_angle, -1):
                s2.duty_u16(duty * 100)
                time.sleep_ms(10)
            
            for duty in range(end_angle, start_angle, -1):
                s1.duty_u16(duty * 100)
                time.sleep_ms(10)
                
        
utime.sleep_ms(500) 