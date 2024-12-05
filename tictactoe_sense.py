from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
e = (255, 255, 255)
l = (0, 0, 0)

board = [
        e, e, l, e, e, l, e, e,
        e, e, l, e, e, l, e, e,
        l, l, l, l, l, l, l, l,
        e, e, l, e, e, l, e, e,
        e, e, l, e, e, l, e, e,
        l, l, l, l, l, l, l, l,
        e, e, l, e, e, l, e, e,
        e, e, l, e, e, l, e, e,
        ]

def r_rgb():
    return (randint(0,255), randint(0,255), randint(0,255))

def random_pixels():
    pixels = [
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), 
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), 
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), 
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), 
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), 
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), 
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), 
            r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb(), r_rgb()
            ]
    return pixels
    
while True:
    acceleration = sense.get_accelerometer_raw()
    x_raw = acceleration['x']
    y_raw = acceleration['y']
    z_raw = acceleration['z']
    x_round = round(x_raw)
    y_round = round(y_raw)
    z_round = round(z_raw)
    x_abs = abs(x_raw)
    y_abs = abs(y_raw)
    z_abs = abs(z_raw)

    if x_abs > 1 or y_abs > 1 or z_abs > 1:
        sense.set_pixels(random_pixels())
    else:
        sense.set_pixels(board)

    sleep(.1)

    

