from dataclasses import dataclass

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, Text, Date
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import registry, relationship
from datetime import datetime


mapper_registry = registry()

@mapper_registry.mapped
@dataclass
class Vibes:
	__table__ = Table(
		"vibes",
		mapper_registry.metadata,
		Column("id", Integer, primary_key=True),
		Column("parent_id", Integer, ForeignKey("vibes.id"), nullable=True, default=None ),
		Column("title", Text),
		Column("contents", Text, nullable=False),
		Column("upvotes", Integer),
		Column("total_votes", Integer),
		Column("sentiment", Integer),
		Column("source_url", String, nullable=False),
		Column("last_updated", Date(), nullable=False)
	)
	title: str
	contents: str
	upvotes: int
	total_votes: int
	sentiment: int
	source_url: str
	related = relationship('Vibes', remote_side=[__table__.c.id])
	last_updated: datetime
