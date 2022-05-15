from screen_setup import ScreenSetup

class Main:
	def __init__(self) -> None:
		# setup class
		pass

	def setup(self) -> None:
		# setup stuff.
		pass

	def controller(self) -> None:
		# control project
		scr = ScreenSetup()
		# start screen setup
		scr.setup('initialize')

		scr.display()

		# start screen destruct.
		scr.setup('destruct')


		

if __name__ == '__main__':
	main = Main()
	main.setup()