from sqlalchemy import create_engine
from Tables import mapper_registry

def main():
    try:
        # Create a database engine
        engine = create_engine('sqlite:///my_database.db')

        # Connect to the database
        connection = engine.connect()

        #Add actual functionality from other files here (potentially a driver class)
        mapper_registry.metadata.create_all(engine)

    except Exception as e:

        print(e)
        print("Connection Failed")
    
    finally:
        connection.close()


if __name__ == "__main__":
    main()
