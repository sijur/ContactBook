from query_builder import QueryBuilder
class SelectQuery(QueryBuilder):

	def setup(self, **kwargs) -> str:
		return self.select(kwargs)

	def select(self, **kwargs) -> str:
		
		query = "SELECT '{}' FROM {} ".format(kwargs['columns'], kwargs['table'])
		if 'where' in kwargs.keys():
			query += "WHERE '{}' ".format(kwargs['where'])
		
		if 'order' in kwargs.keys():
			query += "ORDER BY {} ".format(kwargs['order'])
		
		if 'list_direction' in kwargs.keys():
			query += "{} ".format(kwargs['list_direction']).upper()

		if 'limit' in kwargs.keys():
			query += "LIMIT {}, {} ".format(kwargs['limit'][0], kwargs['limit'][1])
		
		query += ';'
		
		self.sendQuery(query)