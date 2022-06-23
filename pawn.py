from djitellopy import Tello
from time import sleep


def first_step(drone):
    drone.move_forward(80)


def step(drone):
    drone.move_forward(40)


def attack_right(drone):
    drone.rotate_clockwise(45)
    drone.move_forward(56)
    drone.rotate_counter_clockwise(45)

