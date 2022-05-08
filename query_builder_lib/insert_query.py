import abc

from query_builder import QueryBuilder
from select_query import SelectQuery

class InsertQuery(QueryBuilder):    
	def insert(self) -> str:
		# does the record exist?
		# should we create a new one?
		# if so, get the last record
		# query for last record.

		select = SelectQuery()
		id = select.select(columns = 'id', table = 'name', order_by = 'id', list_direction = 'desc', limit = [0, 1])

		print(id)

i = InsertQuery()
i.insert()