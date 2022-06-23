from djitellopy import Tello
from time import sleep


def first_move(drone):
    drone.move_forward(80)
    sleep(1)


def move(drone):
    drone.move_forward(40)
    sleep(1)


def attack_right(drone):
    drone.rotate_clockwise(45)
    drone.move_forward(56)
    drone.rotate_counter_clockwise(45)
    sleep(1)


def attack_left(drone):
    drone.rotate_counter_clockwise(45)
    drone.move_forward(56)
    drone.rotate_clockwise(45)
    sleep(1)