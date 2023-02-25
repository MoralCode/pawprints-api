import sqlalchemy as db

def main():
    try:
        # Create a database engine
        engine = db.create_engine('sqlite:///my_database.db')

        # Connect to the database
        connection = engine.connect()

        #Add actual functionality from other files here (potentially a driver class)

    except Exception at e:

        print(e)
        Print("Connection Failed")
    
    finally:
        connection.close()
