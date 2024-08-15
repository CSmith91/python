# for windows, requires an install
# open cmd and type 'pip install windows-curses'
import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    #stdscr - standard output screen
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
        
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color) # i will get incremented by 1

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip() # strip removes the invisible \n carriage return

def wpm_test(stdscr):
    target_text = load_text()    
    current_text = []
    wpm = 0
    start_time = time.time() # time that's passed since a particular date in the 70's (or thereabouts)
    stdscr.nodelay(True) # required to ensure timer runs even when user doesnt type

    while True:
        time_elapsed = max(time.time() - start_time, 1) # gives us the time passed. max prevents a 0 division error on init by choosing 1 if its bigger
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) # converting chars/minute. Average word has 5 letters
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh() # refreshes the screen so the user can see their input on the screen

        # we need to convert the list to a string
        # we can then end the game
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # due to nodelay, we need to catch any exceptions
        # on init, there is no key typed
        try:
            key = stdscr.getkey()
        except:
            continue

        # escape key (ASCII #) allows user to exit
        if ord(key) == 27:
            break

        # check if user types backspace (for all different os)
        if key in("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop() # remove the last charatcer from the list
        elif len(current_text) < len(target_text):
            current_text.append(key)

        
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue.")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main) #calls this function while init content in module
