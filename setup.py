from setuptools import setup, find_packages
setup(
    name="wtfrit_storage_schema",
    version="0.1.1",
    packages=find_packages(),
    install_requires=['alembic', 'sqlalchemy']
)