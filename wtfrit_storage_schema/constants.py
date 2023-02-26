from os import path
import pkg_resources
ROOT_PATH = path.dirname(__file__)

ALEMBIC_CFG_PATH = pkg_resources.resource_filename('wtfrit_storage_schema', 'alembic.ini')#path.join(ROOT_PATH, "./alembic.ini")
MIGRATIONS_DIR = pkg_resources.resource_filename('wtfrit_storage_schema', 'migrations')#path.join(ROOT_PATH, "migrations")