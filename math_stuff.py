class MathStuff:
	def __init__(self) -> None:
		pass

	def total_menu_width(self, menu) -> int:
		width = 0
		for row in menu:
			width = (width, len(row))[width < len(row)]
		
		return width

	def get_x(self, w, width) -> int:
		# w = the width of the screen
		# width is the width of the text
		# `//` is divide but round down
		# (e.g. 15/4 = 3.75, but 15//4 = 3)

		return w//2 - width//2
	
	def get_y(self, h, menu, idx) -> int:
		# h = height of the screen

		y = h//2 - len(menu)//2 + idx

		if idx == len(menu) - 1:
			y += 1
		
		return y