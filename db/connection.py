import sqlite3


def start_db(db_name = "./db/database.db", schema_file =  "./db/schema.sql") -> bool:
    try:
        conn = sqlite3.connect(db_name)
        access_db = conn.cursor()

        # file = open(schema_file, 'r')
        # buffer = file.read()
        # file.close()

        with open(schema_file, 'r') as file:
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
