import curses
class InitializeScreen:
	def __init__(self, stdscr) -> None:
		self.stdscr = stdscr

	def setup(self) -> None:
		# hide the cursor
		curses.curs_set(0)

		# initiate a color pair, black and white
		curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

		# clear the screen
		self.stdscr.clear()

		# startup the screen
		self.startup()
	
	def startup(self) -> None:
		stdscr = self.stdscr
		curses.noecho()
		curses.cbreak()
		stdscr.keypad(True)