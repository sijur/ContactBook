import pymysql.cursors
import toml

class DatabaseUpkeep:
	def __init__(self) -> None:
		# get db settings
		self.db_settings = self._db_settings()

	def _db_settings(self) -> dict:
		data = toml.load("config.toml")
		database = data['database']

		return {
			"host": database['server'],
			"user": database['username'],
			"password": database['password'],
			"port": database['port'],
			"db_name": 'contact_book_db',
		}
	
	def mysql_connect(self, query, limit) -> str:
		db_settings = self.db_settings
		db = pymysql.connect(host=db_settings['host'], user=db_settings['user'], password=db_settings['password'], database=db_settings['db_name'])

		with db:
			with db.cursor() as cursor:
				sql = query
				cursor.execute(sql)
				if limit == 'all':
					result = cursor.fetchall()
				else:
					result = cursor.fetchone()
				print(result)
		
db = DatabaseUpkeep()
db.mysql_connect("select * from names;", "all")
# db.mysql_connect("select * from names where id = 1;", "1")
