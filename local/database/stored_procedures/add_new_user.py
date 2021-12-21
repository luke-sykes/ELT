import psycopg2
from config import config


def add_new_user(user_id, user_data):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("CALL add_new_user(%s,%s)", (user_id, user_data))
        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
