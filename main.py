# Runs __init__.py in the package package(folder).
import package

import curses
import time
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)

    stdscr.clear()
    # stdscr.addstr(1, 1, " Mosyle Manager ", RED_AND_WHITE | curses.A_BOLD)
    # stdscr.refresh()
    # stdscr.getch()

    for i in range(100):
        stdscr.clear()
        color = BLUE_AND_YELLOW
        if i % 3 == 1:
            color = GREEN_AND_BLACK
        if i % 3 == 2:
            color = RED_AND_WHITE

        stdscr.addstr(1, 1, f" Count: {i} ", color | curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()


wrapper(main)

