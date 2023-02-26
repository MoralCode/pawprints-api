from setuptools import setup, find_packages
setup(
    name="wtfrit_storage_schema",
    version="0.1.1",
    packages=find_packages(),
    package_dir={'': '.'},
    package_data={'wtfrit_storage_schema': ['migrations/**/*']},
    include_package_data=True,
    install_requires=['alembic', 'sqlalchemy'],
)