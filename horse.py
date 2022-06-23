from djitellopy import Tello
from time import sleep
import math


kletka = 40


def move_up_left(drone):
    drone.move_forward(kletka)
    drone.move_left(kletka)
    drone.move_left(kletka)


def move_left_up(drone):
    drone.move_left(kletka)
    drone.move_forward(kletka)
    drone.move_forward(kletka)


def move_up_right(drone):
    drone.move_forward(kletka)
    drone.move_right(kletka)
    drone.move_right(kletka)


def move_right_up(drone):
    drone.move_right(kletka)
    drone.move_forward(kletka)
    drone.move_forward(kletka)


def move_down_left(drone):
    drone.move_back(kletka)
    drone.move_left(kletka)
    drone.move_left(kletka)


def move_left_down(drone):
    drone.move_left(kletka)
    drone.move_back(kletka)
    drone.move_back(kletka)


def move_down_right(drone):
    drone.move_back(kletka)
    drone.move_right(kletka)
    drone.move_right(kletka)


def move_right_down(drone):
    drone.move_right(kletka)
    drone.move_back(kletka)
    drone.move_back(kletka)
