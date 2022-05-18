from screen_setup import ScreenSetup


class DisplayScreen(ScreenSetup):
	def __init__(self) -> None:
		super().__init__()
	
	def display(self, stdscr: object) -> None:
		# currently we're using the key, I'll want to change this so that
		# the menu will know where it's at based on the current choice,
		# not because of a key which could potentially become inaccurate.

		# set current menu index
		idx = 0

		# find out which menu we're on
		# retrieve current menu
		# and print it.

		# loop until user exits
		while 1:
			# get user choice (new key)
			key = stdscr.getch()

			# prepare the screen (currently clearing it)
			self._prepare_screen(stdscr)

			# figure out what action is happening if a key is pressed.
			# new class for the key press action

			# redraw the menu should the user press a key.
			# find out which menu we're on
			# retrieve current menu
			# and print it.