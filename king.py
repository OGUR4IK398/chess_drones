from djitellopy import Tello
from time import sleep
import math

kletka = 40
gradus = 0


def left(drone):
    drone.move_left(kletka)


def m_up(drone):
    drone.move_forward(kletka)


def right(drone):
    drone.move_right(kletka)


def down(drone):
    drone.move_back(kletka)


def left_up(drone):
    gradus = 45
    drone.rotate_counter_clockwise(gradus)
    drone.move_forward(kletka)
    drone.rotate_counter_clockwise(-gradus)
    gradus = 0


def right_up(drone):
    gradus = 45
    drone.rotate_clockwise(gradus)
    drone.move_forward(kletka)
    drone.rotate_clockwise(-gradus)
    gradus = 0


def right_down(drone):
    gradus = 45
    drone.rotate_counter_clockwise(gradus)
    drone.move_back(kletka)
    drone.rotate_counter_clockwise(-gradus)
    gradus = 0


def left_down(drone):
    gradus = 45
    drone.rotate_clockwise(gradus)
    drone.move_back(kletka)
    drone.rotate_clockwise(-gradus)
    gradus = 0


def short_castling(drone):
    drone.move_right(2 * 40)


def long_castling(drone):
    drone.move_left(2 * 40)



