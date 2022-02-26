import curses

class Menu:
    def __init__(self) -> None:
        pass

    def setup(self, lvl) -> str:
        return self.getMenu(lvl)
    
    def getMenu(self, lvl) -> str:
       menu = {
           0: ["List contacts", "Create new address book", 'Exit',],
       }

       return menu[lvl]