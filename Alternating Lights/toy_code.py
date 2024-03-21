# https://github.com/blaz-r/pi_pico_neopixel

# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from neopixel import Neopixel

def run_toy():
    print("Running toy code")
    
    
    pixels = Neopixel(100, 0, 28, "RGB")
    #pixels[10] = (20, 20, 20)
    #pixels.set_pixel(3, (150, 0, 0))
    #pixels.fill((10,10,0))
    
    #pixels.clear()
    #pixels.show()
    
   # while True:
    #    print("Fill")
    #    pixels.fill((0, 50, 0))
     #   pixels.show()
    #  time.sleep(1)
     #   print("Clear")
      #  pixels.fill((50, 0, 0))
       # pixels.show()
        #time.sleep(1)
       # pixels.fill((0, 0, 50))
       
       #pixels.show()
       # time.sleep(1)
        
    hue = 0
    while True:
        color = pixels.colorHSV(hue, 255, 150)
        pixels.fill(color)
        pixels.show()
        
        hue += 150
       # break
