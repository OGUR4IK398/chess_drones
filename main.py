from djitellopy import Tello
from time import sleep
import math
# Фигуры
import pawn, elephant, tower, queen, horse, king


drone = Tello()
drone.connect()
print(drone.get_battery())

drone.takeoff()
sleep(1)

drone_type = input()

while True:
    cmd = input()

    # Проверка и получение кол-ва шагов
    if len(cmd.split()) > 1:
        steps = int(list(cmd.split())[1])
        cmd = list(cmd.split())[0]

    if drone_type == "pawn":
        if cmd == "first_move":
            pawn.first_move(drone)
        elif cmd == "move":
            pawn.move(drone)
        elif cmd == "attack_right":
            pawn.attack_right(drone)
        elif cmd == "attack_left":
            pawn.attack_left(drone)

    elif drone_type == "horse":
        if cmd == "move_up_left":
            horse.move_up_left(drone)
        elif cmd == "move_left_up":
            horse.move_left_up(drone)
        elif cmd == "move_up_right":
            horse.move_up_right(drone)
        elif cmd == "move_right_up":
            horse.move_right_up(drone)
        elif cmd == "move_down_left":
            horse.move_down_left(drone)
        elif cmd == "move_left_down":
            horse.move_left_down(drone)
        elif cmd == "move_down_right":
            horse.move_down_right(drone)
        elif cmd == "move_right_down":
            horse.move_right_down(drone)

    elif drone_type == "elephant":
        if cmd == "right_forward_move":
            elephant.right_forward_move(drone, steps)
        elif cmd == "right_back_move":
            elephant.right_back_move(drone, steps)
        elif cmd == "left_forward_move":
            elephant.left_forward_move(drone, steps)
        elif cmd == "left_back_move":
            elephant.left_back_move(drone, steps)

    elif drone_type == "tower":
        if cmd == "forward_move":
            tower.forward_move(drone, steps)
        elif cmd == "back_move":
            tower.back_move(drone, steps)
        elif cmd == "right_move":
            tower.right_move(drone, steps)
        elif cmd == "left_move":
            tower.left_move(drone, steps)
        elif cmd == "short_castling":
            tower.short_castling(drone)
        elif cmd == "long_castling":
            tower.long_castling(drone)

    elif drone_type == "queen":
        if cmd == "forward_move":
            queen.forward_move(drone, steps)
        elif cmd == "back_move":
            queen.back_move(drone, steps)
        elif cmd == "right_move":
            queen.right_move(drone, steps)
        elif cmd == "left_move":
            queen.left_move(drone, steps)
        elif cmd == "right_forward_move":
            queen.right_forward_move(drone, steps)
        elif cmd == "right_back_move":
            queen.right_back_move(drone, steps)
        elif cmd == "left_forward_move":
            queen.left_forward_move(drone, steps)
        elif cmd == "left_back_move":
            queen.left_back_move(drone, steps)

    elif drone_type == "king":
        if cmd == "left":
            king.left(drone)
        elif cmd == "right":
            king.right(drone)
        elif cmd == "m_up":
            king.m_up(drone)
        elif cmd == "down":
            king.down(drone)
        elif cmd == "left_up":
            king.left_up(drone)
        elif cmd == "right_up":
            king.right_up(drone)
        elif cmd == "left_down":
            king.left_down(drone)
        elif cmd == "right_down":
            king.right_down(drone)
        elif cmd == "short_castling":
            king.short_castling(drone)
        elif cmd == "long_castling":
            king.long_castling(drone)

    if cmd == "end_ flight":
        drone.land()
        break
    sleep(1)