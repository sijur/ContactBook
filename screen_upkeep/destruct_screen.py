import curses

class DestructScreen:
	def __init__(self, stdscr) -> None:
		self.stdscr = stdscr
	
	def setup(self) -> None:
		self.conclusion()
	
	def conclusion(self) -> None:
		stdscr = self.stdscr
		curses.nocbreak()
		stdscr.keypad(False)
		curses.echo()
		curses.endwin()