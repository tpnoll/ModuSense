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
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
            helper.blink_board(1,1)
            # Turn the servo motor
            helper.drive_servo(40,130)
        else:
            helper.drive_servo(130,40)
        
utime.sleep_ms(500) 