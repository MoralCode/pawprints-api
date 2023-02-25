from dataclasses import dataclass

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, Text, Date
from sqlalchemy import Table


mapper_registry = registry()

@mapper_registry.mapped
@dataclass
class RedditPost:
	__table__ = Table(
        "reddit_posts",
        mapper_registry.metadata,
        Column("post_id", Integer, primary_key=True),
        Column("contents", Text),
        Column("date", Date()),
    )
	identifier: int
	contents: str
	
