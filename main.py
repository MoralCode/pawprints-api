from Tables import Vibes, mapper_registry
from sqlalchemy import create_engine

class Database():
	# Create a database engine
	
	def __init__(self):
		self.engine = create_engine('sqlite:///my_database.db')

	def initialize(self):
		#Add actual functionality from other files here (potentially a driver class)
		# Check if the table has been created
		table_exists_before = Vibes.name in metadata.tables
		mapper_registry.metadata.create_all(self.engine)
		table_exists_after = Vibes.name in metadata.tables

		if not table_exists_before and table_exists_after:
			# new tables created, version stamp the DB
			self.stamp()
	
	def stamp(self):
		# load the Alembic configuration and generate the
		# version table, "stamping" it with the most recent rev:
		from alembic.config import Config
		from alembic import command
		alembic_cfg = Config("./alembic.ini")
		command.stamp(alembic_cfg, "head")

	
