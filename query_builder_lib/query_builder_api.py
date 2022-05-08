import importlib
class QueryBuilderAPI:
	def __init__(self) -> None:
		pass

	def find_route(self, **kwargs) -> str:
		type = kwargs['type']
		route = self.get_routes(type)
		mod_name = route[type][0]
		
		mod = importlib.import_module(mod_name)
		print(mod)

		# return mod.route[0](self, kwargs)
	
	def get_routes(self, type) -> dict:
		routes = {
			'select': ['select_query', 'SelectQuery'],
			'insert': ['insert_query', 'InsertQuery'],
		}

		if type in routes:
			return {type: routes[type]}

if __name__ == '__main__':

	q = QueryBuilderAPI()
	q.find_route(type = 'select', columns = '*', table = 'name')