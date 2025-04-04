"""
File: Steeplechase.py
Name: Veronica
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition:Karel is on the left side of the world facing East
    post-condition:Karel is on the right side of the world
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is on the left side of the wall facing East
    post-condition:Karel is on the left side of the wall facing East
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def cross():
    """
    pre-condition:Karel is on the left side of the wall facing East
    post-condition:Karel is on the left side of the wall facing South
    """
    move()
    turn_right()


def down():
    """
    pre-condition:Karel is on the right side of the wall facing South
    post-condition:Karel is on the left side of the wall facing East
    """
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
