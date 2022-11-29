# import libraries for arduino
import time

from pymata4 import pymata4

# echo pin for input
echo = 2

# trigger pin for output
trig = 8

board = pymata4.Pymata4()


def output_data(data):
    print("Distance in CM:", data)


# use this function for setup pin
board.set_pin_mode_sonar(trig, echo, output_data)

while True:
    try:
        time.sleep(1)
        board.sonar_read(trig)
    except Exception:
        board.shutdown()
