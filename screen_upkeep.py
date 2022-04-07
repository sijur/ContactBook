import curses
from curses import wrapper
from math_stuff import MathStuff

from menu import Menu

class ScreenUpkeep: 
    def __init__(self) -> None:
        self.setup()

    def setup(self) -> None:
        # set up the screen variable.
        self.stdscr = curses.initscr()

    # setup of curses.
    def start(self) -> None:
        stdscr = self.stdscr
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
    
    # this undoes the things we did in setup (start)
    def end(self) -> None:
        stdscr = self.stdscr
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
    
    # a function to call the actual display function,
    # but through the wrapper so we don't have weird
    # errors if something goes wrong.
    def display(self) -> None:
        wrapper(self.display_menu)
    
    def display_menu(self, stdscr) -> None:
        # hide the cursor
        curses.curs_set(0)

        # initiate a color pair, black and white
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # clear the screen
        stdscr.clear()

        # initiate the menu class.
        m = Menu()
        # get the top level menu
        menu = m.setup(0)

        # set the current index for the menu.
        current_row_idx = 0
        # create the menu (adding to the string which will be called
        # in a bit)
        self.create_menu(stdscr, menu, current_row_idx)

        # loop until user exits
        while 1:
            # get the current key and pass it to a variable
            # to be referred to until the end.
            key = stdscr.getch()

            # clear the screen
            stdscr.clear()

            # if the user presses the "up" arrow and
            # they're not already at the top
            if key == curses.KEY_UP and current_row_idx > 0:
                # decrease the current_row_idx by 1.
                current_row_idx -= 1
            # if the user presses the down arrow and they're not
            # at the bottom
            elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
                # increase the current_row_idx by 1.
                current_row_idx += 1
            # if the user presses the enter key
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # if the user is at the bottom of the menu
                # or at the exit option quit the program.

                # ToDo: this will have to be changed at some point
                # since the quit option may have to change.
                if menu[current_row_idx] == "Exit":
                    quit()
                
                # clear the screen
                stdscr.clear()
                # display text regarding what the user chose.
                stdscr.addstr(0,0, 'You clicked on {}.'.format(menu[current_row_idx]), curses.color_pair(0))

                # refresh the screen to redraw it.
                stdscr.refresh()
                
                # return the character that the user pressed.
                stdscr.getch()

            # redraw the menu
            self.create_menu(stdscr, menu, current_row_idx)
        
        # refresh the screen to redraw it.
        stdscr.refresh()
        # return the character that the user pressed.
        stdscr.getch()
    
    def create_menu(self, stdscr, menu, selected_row_idx) -> None:
        # initiate the MathStuff class.
        math = MathStuff()
        
        # total width of the menu itself, nothing else.
        width = math.total_menu_width(menu)

         # get the height and width of the screen.
        h, w = stdscr.getmaxyx()

        # clear the screen
        stdscr.clear()

        for idx, row in enumerate(menu):
            # for each item we need to get the center position.
            
            # get the vertical position on the screen
            y = math.get_y(h, menu, idx)
            
            # get the greatest width of the text
            x = math.get_x(w, width)

            self.highlightSelection(y, x, row, stdscr, selected_row_idx, idx)
            
    
    def highlightSelection(self, y, x, row, stdscr, row_idx, idx) -> None:
        # highlight the current selection otherwise don't.
        if idx == row_idx:
            stdscr.addstr(y, x, row, curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)