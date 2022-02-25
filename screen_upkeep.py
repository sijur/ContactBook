import curses
from curses import wrapper

from menu import Menu

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
    
    def display_menu(self, stdscr) -> None:
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        stdscr.clear()

        m = Menu()
        menu = m.setup(0)

        current_row_idx = 0

        self.create_menu(stdscr, menu, current_row_idx)

        while 1:
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row_idx == len(menu) - 1:
                    quit()
                
                stdscr.clear()
                stdscr.addstr(0,0, 'You clicked on {}.'.format(menu[current_row_idx]), curses.color_pair(0))
                stdscr.refresh()
                stdscr.getch()

            self.create_menu(stdscr, menu, current_row_idx)
        stdscr.refresh()
        stdscr.getch()
    
    def create_menu(self, stdscr, menu, selected_row_idx) -> None:
        width = self.getWidth(menu)
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(menu):
            x = w//2 - width//2
            if idx == len(menu) - 1:
                y = h//2 - len(menu)//2 + (idx + 1)
            else:
                y = h//2 - len(menu)//2 + idx

            if idx == selected_row_idx:
                stdscr.addstr(y, x, row, curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
    
    def getWidth(self, menu) -> None:
        width = 0
        for row in menu:
            width = (width, len(row))[width < len(row)]
        
        return width

    