import curses

class KeyPress:
	def __init__(self, ) -> None:
		pass
	
	def setup(self, *args) -> None:
		key = args[0]
		row_idx = args[1]
		menu = args[2]
		stdscr = args[3]

		# if the user presses the "up" arrow and
		# they're not already at the top
		if key == curses.KEY_UP and row_idx > 0:
			# decrease the row_idx by 1.
			row_idx -= 1
		# if the user presses the down arrow and they're not
		# at the bottom
		elif key == curses.KEY_DOWN and row_idx < len(menu) - 1:
			# increase the row_idx by 1.
			row_idx += 1
		# if the user presses the enter key
		elif key == curses.KEY_ENTER or key in [10, 13]:
			# if the user is at the bottom of the menu
			# or at the exit option quit the program.

			if menu[row_idx] == "Exit":
				quit()
			
			# clear the screen
			stdscr.clear()
			# display text regarding what the user chose.
			stdscr.addstr(0,0, 'You clicked on {}.'.format(menu[row_idx]), curses.color_pair(0))

			# refresh the screen to redraw it.
			stdscr.refresh()
			
			# return the character that the user pressed.
			stdscr.getch()
		
		return row_idx

