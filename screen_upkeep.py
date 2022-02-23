import curses
from curses import wrapper

class ScreenUpkeep: 
    def __init__(self) -> None:
        self.setup()

    def setup(self) -> None:
        self.stdscr = curses.initscr()

    def start(self) -> None:
        stdscr = self.stdscr
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
    
    def end(self) -> None:
        stdscr = self.stdscr
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
    
    def display(self) -> None:
        wrapper(self.display_menu)
    
    def display_menu(self, msg) -> None:
        stdscr = self.stdscr
        msg = "You started curses."
        stdscr.addstr(0, 0, msg)
        stdscr.refresh()
        stdscr.getch()