from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear((0, 0, 0))

def rp():
    return (randint(0,255), randint(0,255), randint(0,255) )

while True:
    '''
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))
    random_pixel = (random.randint(0, 7), random.randint(0, 7))

    # set pixel color
    sense.set_pixel(random_pixel[0], random_pixel[1], random_color)
    time.sleep(.1)
    '''

    pixels = [
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp(), 
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp(), 
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp(), 
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp(), 
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp(), 
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp(), 
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp(), 
            rp(), rp(), rp(), rp(), rp(), rp(), rp(), rp()
            ]

    sense.set_pixels(pixels)
    sleep(.1)


