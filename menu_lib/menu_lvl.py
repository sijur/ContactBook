from ..menu import Menu


class MenuLvl(Menu):
	def setup(self, lvl) -> str:
		return self.get_menu(lvl)
	
	def get_menu(self, lvl) -> str:
		menu = {
			0: ['List contacts', 'Add new contact', 'Exit',],
		}

		return menu[lvl]