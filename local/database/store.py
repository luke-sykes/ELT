from local.database.connection.connect import DatabaseLayer


def store_data():
    with DatabaseLayer() as database:
        database.add_data()
    return None
