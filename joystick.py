from sense_hat import SenseHat
from random import randint, choice
from time import sleep
from time import time

sense = SenseHat()
bl = (0, 0, 0)
wh = (255, 255, 255)
gr = (0, 255, 0)
r = (255, 0, 0)
board_color = bl
timer = time()
directions = ('left', 'right', 'down', 'up')
s_head = [gr, [randint(3,4), randint(3,4)]]
s_dir = choice(directions)
a_starts = (0, 1, 2, 5, 6, 7)
apple = [r, choice(a_starts), choice(a_starts)]
apples_eaten = 0
tail = []
t_col = (0, 255, 31)

def gr_bg_helper():
    return (randint(0,100), randint(150,255), randint(0,100))

# mode lists: [speed, snake_color, apple_color, background, background change?]
easy_mode = [.2, gr, r, bl, False]
medium_mode = [.15, gr, r, bl, True]
hard_mode = [.1, gr, r, gr_bg_helper(), True]
sigma_rizz = [.08, gr, r, gr_bg_helper(), True]
modes = {
        'Easy': easy_mode,
        'Medium': medium_mode,
        'Hard': hard_mode,
        'Sigma Rizz': sigma_rizz
        }
mode_ops = list(modes.keys())

def set_head():
    global sense, s_head
    sense.set_pixel(s_head[1][0], s_head[1][1], s_head[0])
    
def set_tail():
    global tail, apples_eaten, t_col
    if len(tail) > apples_eaten:
        del tail[0]
    for tail_segment in tail:
        sense.set_pixel(tail_segment[0], tail_segment[1], t_col)

def set_apple():
    global apple
    sense.set_pixel(apple[1], apple[2], apple[0])

def new_apple():
    global apple, tail
    tail_x = []
    tail_y = []
    for seg in tail:
        tail_x.append(seg[0])
        tail_y.append(seg[1])
    bad_apple = True
    while bad_apple:
        x = choice([i for i in range(0,7) if i != s_head[1][0]])
        y = choice([i for i in range(0,7) if i != s_head[1][1]])
        if [x, y] not in tail:
            apple = [r, x, y]
            bad_apple = False
        
def check_eaten():
    global s_head, apple, apples_eaten
    if (s_head[1][0] == apple[1] and s_head[1][1] == apple[2]):
        set_head()
        new_apple()
        apples_eaten += 1
    return True
    
def check_collision():
    global s_head, tail
    if s_head[1] in tail:
        return True

def board_color_helper(mode):
    if mode == 'Easy':
        return (0,0,0)
    elif mode == 'Medium':
        return (randint(0,200), randint(0,200), randint(0,200))
    else:
        return gr_bg_helper()

def loop_helper(coord, d):
    if coord == 0 and d == -1:
        return 7
    elif coord == 7 and d == 1:
        return 0
    else:
        return coord + d

def switcheroo(notnormal):
    global t_col
    if notnormal:
        s_head[0] = r
#        t_col = r
        apple[0] = gr
    if not notnormal:
        s_head[0] = gr
#        t_col = gr
        apple[0] = r

def update_board(s_dir):
    global sense, bl, s_head, tail
    sense.clear(board_color)
    set_tail()
    set_head()
    set_apple()
    match s_dir:
        case 'left':
            s_head[1][0] = loop_helper(s_head[1][0], -1)
        case 'right':
            s_head[1][0] = loop_helper(s_head[1][0], 1)
        case 'down':
            s_head[1][1] = loop_helper(s_head[1][1], 1)
        case 'up':
            s_head[1][1] = loop_helper(s_head[1][1], -1)
    if (check_collision()):
        reset()
    if (check_eaten()):
        tail.append([s_head[1][0], s_head[1][1]])

def reset():
    global tail, s_head, apples_eaten, apple, timer
    for _ in range(25):
        sense.clear((randint(0,255), randint(0,255), randint(0,255)))
        sleep(0.05)
    sense.clear(bl)
    game_over_message = 'Score: ' + str(apples_eaten) + '   '
    sense.show_message(game_over_message, text_colour=(100,255,100), scroll_speed=0.035)
    sense.show_message('Press any button to restart', text_colour=(100, 255, 100), scroll_speed=0.035)
    start = time()
    timer = time()
    iterator = 5
    while True:
        if (time() - timer) > 1:
            timer = time()
            sense.show_message(str(iterator), text_colour=(100,255,100), scroll_speed=0.035)
            iterator -= 1
        if (time() - start) > 6:
            exit()
        if len(sense.stick.get_events()) > 0:
            break
    apples_eaten = 0
    apple = [r, choice(a_starts), choice(a_starts)] 
    s_head = [gr, [randint(3,4), randint(3,4)]] 
    tail = [] 
    gameloop()

def gameloop():
    global timer, s_head, s_dir, board_color, sense, modes
    sense.set_pixel(s_head[1][0], s_head[1][1], s_head[0])
    sense.show_message('Pick your game mode!', text_colour=(100,255,100), scroll_speed=0.035)
    picked = False
    index = 0
    
    while not picked:
        sense.show_message(mode_ops[index], text_colour=(100,255,100), scroll_speed=0.035)
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'right':
                if index < 3: 
                    index += 1
            elif event.action == 'pressed' and event.direction == 'left':
                if index > 0: 
                    index -= 1
            elif event.action == 'pressed' and event.direction == 'middle':
                picked = True

    choice = mode_ops[index]
    board_color = board_color_helper(choice)
    update_board(s_dir)
    change_timer = time()
    normal = False
    while True:
        if time() > timer + 1: 
            timer = time()
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction != 'middle': 
                if event.direction == 'down' and s_dir != 'right':
                    s_dir = 'left'
                elif event.direction == 'up' and s_dir != 'left':
                    s_dir = 'right'
                elif event.direction == 'left' and s_dir != 'down':
                    s_dir = 'up'
                elif event.direction == 'right' and s_dir != 'up':
                    s_dir = 'down'
            if event.action == 'pressed' and event.direction == 'middle' and modes[choice][4]:
                board_color = board_color_helper(choice)
            if time() - change_timer > 2.5 and choice == 'Sigma Rizz':
                switcheroo(not normal)
                change_timer = time()
                normal = not normal
        
        update_board(s_dir)
        sleep(modes[choice][0])
        

sense.clear(bl)
sense.set_rotation(270)
gameloop()
