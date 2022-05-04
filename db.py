import MySQLdb

import toml

class DatabaseUpkeep:
    def __init__(self) -> None:
        # get db settings
        data = toml.load("config.toml")
        database = data['database']
        self.host = database['server']
        self.user = database['username']
        self.password = database['password']
        self.port = database['port']
    
    

db = DatabaseUpkeep()
