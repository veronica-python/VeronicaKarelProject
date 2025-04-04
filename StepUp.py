"""
File: StepUp.py
Name: Veronica
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *

def turn_right():
    """
    pre-condition:Karel is at the left of the pothole facing East
    post-condition:Karel is at the right of the pothole facing East
    """
    turn_left()
    turn_left()
    turn_left()

def put_99beepers():
    """
    pre-condition:Karel is at the left of the pothole facing East
    post-condition:Karel is at the right of the pothole facing East
    """
    for i in range(99):
        put_beeper()

def main():
    #algorithm
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_99beepers()
    move()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
