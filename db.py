import pymysql.cursors
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
	
	def mysql_connect(self):
		db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db_name)

		with db:
			with db.cursor() as cursor:
				sql = "SELECT * FROM names;"
				cursor.execute(sql)
				result = cursor.fetchone()
				print(result)
		
db = DatabaseUpkeep()
db.mysql_connect()
