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
    
    while True:
        print("Fill")
        pixels.fill((0, 50, 0))
        pixels.show()
        time.sleep(5)
        print("Clear")
        pixels.clear()
        pixels.show()
        time.sleep(5)
        
        
        # OK i can see a signal on the oscope when i put just pixels.show() in a while loop, otherwise i cant
       # break
