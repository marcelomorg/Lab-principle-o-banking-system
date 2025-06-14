import sqlite3

db_path = "./db/database.db"
schema_path = "./db/schema.sql"

def start_db(database = db_path, schema = schema_path) -> bool:
    try:
        conn = sqlite3.connect(database)
        access_db = conn.cursor()

        # file = open(schema_file, 'r')
        # buffer = file.read()
        # file.close()

        with open(schema, 'r') as file:
            buffer = file.read()
            access_db.executescript(buffer)

        conn.commit()
        return True
    
    except Exception as erro:
        print(erro)
        return False
    
    finally:
        if 'conn' in locals():
            conn.close()


def get_connection(database = db_path):
    return sqlite3.connect(database)