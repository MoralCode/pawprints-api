# wtfrit-storage-schema

a central, shared python module for keeping track of the database schema so that it can be used by mutltiple other programs, such as ingest scripts and processing jobs.

This is intended mainly for WTFRIT internal use only (i.e. if you are editing the core of the app or making an ingestion script). If you are looking to make an integration with the data, see the external API (link TBD). 

## Usage

### Migrations
Migrations help ensure that databases generated using older versions of the schema can be upgraded without having to delete and recreate them (and lose data)

If you have an older database and want to upgrade it, run `pipenv run alembic upgrade head`.

#### To create a migration
1. ensure your database is up to date per the above command
2. make your changes to the schema in sqlalchemy
3. Create a new migration with `pipenv run alembic revision --autogenerate -m "<summary of change>"`
4. Inspect the new file in the `migrations/versions` folder to make sure it looks right and only reflects the change you just made to the schema
5. Commit this migration script
6. Rerun the updgrade command from step 1 to ensure that your database has the new schema

The new database schema should now work with whatever code depends on it


## Setup

### Environment variables

