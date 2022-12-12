# import libraries for arduino
import time

from pymata4 import pymata4

# echo pin for input
echo1 = 3
echo2 = 5
echo3 = 7
echo4 = 9
echo5 = 11
echo6 = 13

# trigger pin for output
trig1 = 2
trig2 = 4
trig3 = 6
trig4 = 8
trig5 = 10
trig6 = 12

board = pymata4.Pymata4()


def output_data1(data1):
    print("Distance of 1 in CM:", data1[2])


def output_data2(data2):
    print("Distance of 2 in CM:", data2[2])


def output_data3(data3):
    print("Distance of 3 in CM:", data3[2])


def output_data4(data4):
    print("Distance of 4 in CM:", data4[2])


def output_data5(data5):
    print("Distance of 5 in CM:", data5[2])


def output_data6(data6):
    print("Distance of 6 in CM:", data6[2])


# use this function for setup pin
board.set_pin_mode_sonar(trig1, echo1, output_data1)
board.set_pin_mode_sonar(trig2, echo2, output_data2)
board.set_pin_mode_sonar(trig3, echo3, output_data3)
board.set_pin_mode_sonar(trig4, echo4, output_data4)
board.set_pin_mode_sonar(trig5, echo5, output_data5)
board.set_pin_mode_sonar(trig6, echo6, output_data6)

while True:
    try:
        time.sleep(0.5)
        board.sonar_read(trig1)
        board.sonar_read(trig2)
        board.sonar_read(trig3)
        board.sonar_read(trig4)
        board.sonar_read(trig5)
        board.sonar_read(trig6)
    except Exception:
        board.shutdown()
