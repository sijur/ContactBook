import curses
from curses import wrapper
from screen_upkeep import ScreenUpkeep
from menu import Menu
from math_stuff import MathStuff
from .key_press import KeyPress

class DisplayScreen(ScreenUpkeep):
	def __init__(self) -> None:
		super().__init__()
	
	# a function to call the actual display function,
	# but through the wrapper so we don't have weird
	# errors if something goes wrong.
	def display(self) -> None:
		wrapper(self.display_menu)

	def display_menu(self, stdscr) -> None:
		# initiate screen
		self._initiate_screen(stdscr)

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

			# what to do when a key is pressed.
			key_action = KeyPress()
			current_row_idx = key_action.setup(key, current_row_idx, menu, stdscr)

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