from Tables import Vibes, mapper_registry

class Database():
	# Create a database engine
	
	def __init__(self):
		self.engine = create_engine('sqlite:///my_database.db')

	def initialize(self):
		#Add actual functionality from other files here (potentially a driver class)
        mapper_registry.metadata.create_all(self.engine)
	
	
