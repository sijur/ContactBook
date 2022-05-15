import curses

from screen_upkeep import DestructScreen
from screen_upkeep import InitializeScreen

class ScreenSetup:
	def __init__(self) -> None:
		pass

	def setup(self, action: str) -> None:
		stdscr = curses.initscr()

		if action == 'initialize':
			self._initialize(stdscr)
		elif action == 'destruct':
			self._destruct(stdscr)
		else:
			raise Exception("please include an action.")
	
	def _initialize(self, stdscr: object) -> None:
		screen_init = InitializeScreen(stdscr)
		screen_init.setup()

	def _destruct(self, stdscr: object) -> None:
		screen_destruct = DestructScreen(stdscr)
		screen_destruct.setup()