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


def right_forward_move(drone, steps):
    drone.rotate_clockwise(45)
    drone.move_forward(40 * steps)
    drone.rotate_counter_clockwise(45)
    sleep(1)


def right_back_move(drone, steps):
    drone.rotate_clockwise(135)
    drone.move_forward(40 * steps)
    drone.rotate_counter_clockwise(135)
    sleep(1)


def left_forward_move(drone, steps):
    drone.rotate_counter_clockwise(45)
    drone.move_forward(40 * steps)
    drone.rotate_clockwise(45)
    sleep(1)


def left_back_move(drone, steps):
    drone.rotate_counter_clockwise(135)
    drone.move_forward(40 * steps)
    drone.rotate_clockwise(135)
    sleep(1)