import psycopg2
from local.database.connection.config import config


def connect():
    """
    Connect to the PostgreSQL database server
    :return:
    """

    conn = None
    try:
        params = config()

        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print("PostgreSQL database version:")
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")
