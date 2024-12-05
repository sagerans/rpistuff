import time

old_time = time.time()

while True:
    current_time = time.time()
    if (current_time - old_time) > 1:
        print(current_time)
        old_time = current_time
