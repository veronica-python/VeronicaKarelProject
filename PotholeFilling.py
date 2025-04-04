"""
File: PotholeFilling.py
Name: Veronica
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import*

def main():
    pass
    for i in range(3):
        move()
        go_in()
        put_99beepers()
        go_out()

def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole facing East
    post-condition:Karel is at the pothole facing South
    """
    turn_right()
    move()


def go_out():
    """
    pre-condition:Karel is at the upper left of the pothole facing East
    post-condition:Karel is at the pothole facing South
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()




# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
