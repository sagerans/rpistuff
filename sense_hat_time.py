from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

color = (randint(0,255), randint(0,255), randint(0,255))
background = (255 - color[0], 255 - color[1], 255 - color[2])
new_color = color
new_background = background
rotation = 0

def transition_background(new_background, background):
    iterations = 100
    r_diff = (new_background[0] - background[0]) // iterations
    g_diff = (new_background[1] - background[1]) // iterations
    b_diff = (new_background[2] - background[2]) // iterations
    color = background
    for _ in range(iterations):
        color = (
                abs(color[0] + r_diff),
                abs(color[1] + g_diff),
                abs(color[2] + b_diff)
                )
        sense.clear(color)
        time.sleep(.025)

message = ''
request = input('Type the message you\'d like to display (press Enter for default): ')

while True:
    color = new_color
    background = new_background
    print(color)
    print(background)
    current_time = time.asctime()
    pressure = round(sense.get_pressure(),1)
    temp = round(sense.get_temperature(),1)
    humidity = round(sense.get_humidity(),1)
    if (request):
        message = request
    else:
        message = current_time + '  Temp: ' + str(temp) + 'C  Humidity: ' + str(humidity) + '%  Pressure: ' + str(pressure) + 'mB'
    sense.show_message(message, text_colour=color, back_colour=background, scroll_speed=0.066)
    new_color = (randint(0,255), randint(0,255), randint(0,255))
    new_background = (255 - new_color[0], 255 - new_color[1], 255 - new_color[2])
    transition_background(new_background, background)
    '''
    if rotation < 270:
        rotation += 90
    else:
        rotation = 0
    sense.set_rotation(rotation)
    '''
