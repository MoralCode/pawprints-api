# wtfrit-storage-schema

a central, shared python module for keeping track of the database schema so that it can be used by mutltiple other programs, such as ingest scripts and processing jobs.

This is intended mainly for WTFRIT internal use only (i.e. if you are editing the core of the app or making an ingestion script). If you are looking to make an integration with the data, see the external API (link TBD). 

## Usage

### Creating a migration
pipenv run alembic revision --autogenerate -m "add total_votes column"

### Running migrations

## Setup

### Environment variables

