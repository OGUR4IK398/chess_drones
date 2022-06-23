from djitellopy import Tello
from time import sleep


def forward_move(drone, steps):
    drone.move_forward(40 * steps)
    sleep(1)


def back_move(drone, steps):
    drone.move_back(40 * steps)
    sleep(1)


def right_move(drone, steps):
    drone.move_right(40 * steps)
    sleep(1)


def left_move(drone, steps):
    drone.move_left(40 * steps)
    sleep(1)


def short_castling(drone):
    drone.move_back(40)
    drone.move_left(40 * 2)
    drone.move_forward(40)


def long_castling(drone):
    drone.move_back(40)
    drone.move_right(40 * 2)
    drone.move_forward(40)