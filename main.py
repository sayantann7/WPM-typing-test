import curses
from curses import wrapper
import time
import requests

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to WPM Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(2,0,f"WPM = {wpm}")
    for i,char in enumerate(current):
        correct_char = target[i]
        if char==correct_char:
            stdscr.addstr(0,i,char,curses.color_pair(1))
        else:
            stdscr.addstr(0,i,char,curses.color_pair(2))
    
def wpm_test(stdscr):
    req = requests.get("https://api.quotable.io/random")
    target_text = req.json()["content"]
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time()-start_time,1)
        wpm = round((len(current_text)/(time_elapsed/60))/5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text)==target_text:
            stdscr.nodelay(False)
            break


        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key)==27:
            break
        if key in ("KEY_BACKSPACE", '\b' , "\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(3,0,"You completed the test!")
        stdscr.addstr(4,0,"Press any key to play again!")
        stdscr.addstr(5,0,"Press ESC to close the game!")
        key = stdscr.getkey()
        if ord(key)==27:
            curses.endwin()
            break

wrapper(main)