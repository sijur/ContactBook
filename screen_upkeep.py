import curses
class ScreenUpkeep: 
	def __init__(self) -> None:
		self.setup()
	
	def _initiate_screen(self, stdscr: object) -> None:
		# hide the cursor
		curses.curs_set(0)

		# initiate a color pair, black and white
		curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

		# clear the screen
		stdscr.clear()

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