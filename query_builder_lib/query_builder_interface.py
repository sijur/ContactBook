import abc

class QueryBuilderInterface(metaclass=abc.ABCMeta):
	@classmethod
	def __subclasshook__(cls, subclass):
		return (hasattr(subclass, 'sendQuery') and
				callable(subclass.sendQuery) or
				NotImplemented)

	@abc.abstractmethod
	def sendQuery(self, msg: str) -> str:
		""" return query formatted for the db. """
		raise NotImplementedError