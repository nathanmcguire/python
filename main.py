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

    counter_win = curses.newwin(1, 20, 10, 10)

    stdscr.clear()
    # stdscr.addstr(1, 1, " Mosyle Manager ", RED_AND_WHITE | curses.A_BOLD)
    # stdscr.refresh()
    # stdscr.getch()

    stdscr.addstr("Hello Worlds! ", RED_AND_WHITE | curses.A_BOLD)
    stdscr.refresh()
    #for i in range(100):
    #    counter_win.clear()
    #    color = BLUE_AND_YELLOW
    #    if i % 3 == 1:
    #        color = GREEN_AND_BLACK
    #    if i % 3 == 2:
    #        color = RED_AND_WHITE

    #    counter_win.addstr(f" Count: {i} ", color | curses.A_BOLD)
    #    counter_win.refresh()
    #    time.sleep(0.1)
        
    pad = curses.newwin(100,100)
    stdscr.refresh()
    for i in range (100):
        for j in range (26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_AND_BLACK)
    pad.refresh(0,0,5,5,10,75)
    stdscr.refresh()
    
    stdscr.getch()


wrapper(main)

