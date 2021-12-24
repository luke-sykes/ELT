from database.data_access import DatabaseLayer


def store_data():
    with DatabaseLayer() as database:
        database.add_data()
    return None
