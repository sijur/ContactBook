import curses

class Menu:
    def __init__(self, menu) -> None:
        self.menu = menu

    def setup_menu(self, stdscr, selected_row_idx) -> None:
        menu = self.menu
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = h//2 - len(menu)//2 + idx

            if idx == selected_row_idx:
                stdscr.addstr(y, x, row, curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()
