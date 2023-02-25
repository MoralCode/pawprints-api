from dataclasses import dataclass

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, Text, Date
from sqlalchemy import Table
from sqlalchemy.orm import registry


mapper_registry = registry()

@mapper_registry.mapped
@dataclass
class Vibes:
	__table__ = Table(
		"vibes",
		mapper_registry.metadata,
		Column("id", Integer, primary_key=True),
		Column("title", Text),
		Column("contents", Text, nullable=False),
		Column("upvotes", Integer),
		Column("sentiment", Integer),
		Column("source_url", String, nullable=False),
		Column("last_updated", Date(), nullable=False)
	)
	identifier: int
	title: str
	contents: str
	upvotes: int
	
