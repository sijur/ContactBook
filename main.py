from screen_upkeep import ScreenUpkeep

class Main:
    def __init__(self) -> None:
        # setup class
        pass

    def controller(self) -> None:
        # control project
        # setup curses.
        scr = ScreenUpkeep()
        scr.start()

        scr.display()

        scr.end()

    def setup_curses(self) -> None:
        # setup the menu's screen
        pass

main = Main()
main.controller()