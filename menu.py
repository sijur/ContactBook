import curses

class Menu:
    def __init__(self) -> None:
        pass

    def setup(self, lvl) -> str:
        return self.getMenu(lvl)
    
    def getMenu(self, lvl) -> str:
       menu = {
           0: ["List contacts", "Create new address book", 'Exit',],
       }

       return menu[lvl]

# class Menu:
#     def __init__(self, menu) -> None:
#         self.menu = menu

    # def setup_menu(self, stdscr, selected_row_idx) -> None:
        # menu = self.menu
        # curses.curs_set(0)
        # curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # stdscr.clear()
        # h, w = stdscr.getmaxyx()

        # width of longest item
        # width = self.get_width(menu)

        # for idx, row in enumerate(menu):
        #     x = w//2 - width//2
        #     if idx == len(menu) - 1:
        #         y = h//2 - len(menu)//2 + (idx + 1)
        #     else:
        #         y = h//2 - len(menu)//2 + idx

        #     if idx == selected_row_idx:
        #         stdscr.addstr(y, x, row, curses.color_pair(1))
        #     else:
        #         stdscr.addstr(y, x, row)

        # stdscr.refresh()
    
    # def get_width(self, menu) -> int:
    #     width = 0
    #     for row in menu:
    #         width = (width, len(row))[width < len(row)]
        
    #     return width
    
    # def display_menu(self) -> None:
    #     pass