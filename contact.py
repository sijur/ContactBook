import curses
from curses import wrapper

from menu import Menu

class Contact:
    def __init__(self) -> None:
        self.menu = ['Add Contact', 'Remove Contact', 'Update Contact', 'Exit']

    def setup(self) -> None:
        #initialize curses into stdscr
        stdscr = curses.initscr()

        # initialize curses
        self.initialize_menu(stdscr)

        # display the menu
        wrapper(self.display_menu)

        # terminate curses
        self.terminate_menu(stdscr)
    
    def display_menu(self, stdscr) -> str:
        current_row_idx = 0
        menu = self.menu
        m = Menu(menu)
        m.setup_menu(stdscr, current_row_idx)

        while 1:
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row_idx == len(menu) - 1:
                    break
                
                stdscr.clear()
                stdscr.addstr(0,0, 'You clicked on {}.'.format(menu[current_row_idx]), curses.color_pair(0))
                stdscr.refresh()
                stdscr.getch()

            m.setup_menu(stdscr, current_row_idx)

        stdscr.refresh()
        stdscr.getkey()
    
    def initialize_menu(self, stdscr) -> None:
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

    def terminate_menu(self, stdscr) -> None:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


c = Contact()
c.setup()