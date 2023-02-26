from Tables import Vibes, mapper_registry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

class Database():
	# Create a database engine
	
	def __init__(self, db_name='sqlite:///my_database.db'):
		self.engine = create_engine(db_name)
		self.session = sessionmaker(bind=self.engine)()

	def exists(self):
		inspector = inspect(self.engine)
		tables_status = [inspector.has_table(table.name) for table in mapper_registry.metadata.tables.values()]

		tables_existing = filter(lambda a : a== True, tables_status)
		tables_existing = len(list(tables_existing))
				
		return tables_existing == len(tables_status)

	def initialize(self):
		#Add actual functionality from other files here (potentially a driver class)
		# Check if the table has been created
		table_exists_before = self.exists()
		mapper_registry.metadata.create_all(self.engine)
		table_exists_after = self.exists()

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

	def add(self, object):
		return self.session.add(object)

	def commit(self):
		return self.session.commit()

	def reset_values(self):
		for table in reversed(mapper_registry.metadata.sorted_tables):
			self.session.execute(table.delete())
			self.commit()

	
if __name__ == "__main__":
	db = Database()
	db.initialize()