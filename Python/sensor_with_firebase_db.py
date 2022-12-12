# import libraries for arduino
import time

from pymata4 import pymata4
import pyrebase

config = {
    "apiKey": "AIzaSyBPO3d1apliSjDB_4nlgFT1eJCwBBXF2ZU",
    "authDomain": "park-in-0.firebaseapp.com",
    "databaseURL": "https://park-in-0-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "park-in-0",
    "storageBucket": "park-in-0.appspot.com",
    "messagingSenderId": "886580757201",
    "appId": "1:886580757201:web:384866702ae791f0c63bf0",
    "measurementId": "G-WY5CJTH9WV"
}

firebaseApp = pyrebase.initialize_app(config)
databaseData = firebaseApp.database()


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
    slot1 = True
    # print("Distance in CM:", data6[2])
    if 0 <= data1[2] <= 5:
        slot1 = False
        databaseData.child("DEMO PARKING 1").child("Slots").update({'slot-1': False})
        print(slot1, "1")
    else:
        databaseData.child("DEMO PARKING 1").child("Slots").update({"slot-1": True})


def output_data2(data2):
    slot2 = True
    # print("Distance in CM:", data6[2])
    if 0 <= data2[2] <= 5:
        slot2 = False
        databaseData.child("DEMO PARKING 1").child("Slots").update({'slot-2': False})
        print(slot2, "2")
    else:
        databaseData.child("DEMO PARKING 1").child("Slots").update({"slot-2": True})


def output_data3(data3):
    slot3 = True
    # print("Distance in CM:", data6[2])
    if 0 <= data3[2] <= 5:
        slot3 = False
        databaseData.child("DEMO PARKING 1").child("Slots").update({'slot-3': False})
        print(slot3, "3")
    else:
        databaseData.child("DEMO PARKING 1").child("Slots").update({"slot-3": True})


def output_data4(data4):
    slot4 = True
    # print("Distance in CM:", data6[2])
    if 0 <= data4[2] <= 5:
        slot4 = False
        databaseData.child("DEMO PARKING 1").child("Slots").update({'slot-4': False})
        print(slot4, "4")
    else:
        databaseData.child("DEMO PARKING 1").child("Slots").update({"slot-4": True})


def output_data5(data5):
    slot5 = True
    # print("Distance in CM:", data6[2])
    if 0 <= data5[2] <= 5:
        slot5 = False
        databaseData.child("DEMO PARKING 1").child("Slots").update({'slot-5': False})
        print(slot5, "5")
    else:
        databaseData.child("DEMO PARKING 1").child("Slots").update({"slot-5": True})


def output_data6(data6):
    slot6 = True
    # print("Distance in CM:", data6[2])
    if 0 <= data6[2] <= 5:
        slot6 = False
        databaseData.child("DEMO PARKING 1").child("Slots").update({'slot-6': False})
        print(slot6, "6")
    else:
        databaseData.child("DEMO PARKING 1").child("Slots").update({"slot-6": True})


# use this function for setup pin
board.set_pin_mode_sonar(trig1, echo1, output_data1)
board.set_pin_mode_sonar(trig2, echo2, output_data2)
board.set_pin_mode_sonar(trig3, echo3, output_data3)
board.set_pin_mode_sonar(trig4, echo4, output_data4)
board.set_pin_mode_sonar(trig5, echo5, output_data5)
board.set_pin_mode_sonar(trig6, echo6, output_data6)

while True:
    try:
        time.sleep(1)
        board.sonar_read(trig1)
        board.sonar_read(trig2)
        board.sonar_read(trig3)
        board.sonar_read(trig4)
        board.sonar_read(trig5)
        board.sonar_read(trig6)
    except Exception:
        board.shutdown()
