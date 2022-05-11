from screen_upkeep_lib.screen_display import DisplayScreen

class Main:
	def __init__(self) -> None:
		# setup class
		pass

	def controller(self) -> None:
		# control project
		# setup curses.
		scr = DisplayScreen()
		scr.start()

		scr.display()

		scr.end()

main = Main()
main.controller()