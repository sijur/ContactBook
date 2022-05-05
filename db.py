import pymysql

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
        self.db_name = 'contact_book_db'
    
    def mysql_connect(self) -> None:
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db_name)

        cursor = db.cursor()

        

        db.close()

        
    

db = DatabaseUpkeep()
db.mysql_connect()
