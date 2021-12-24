import psycopg2
import yaml


class DatabaseLayer:
    @staticmethod
    def config(
        file_path="C:\\Users\\Luke\\Documents\\projects\\ELT\\local\\database\\connection\\database.yaml",
    ):
        """
        Open the given yaml file in read only mode.
        :param file_path:
        :return: Safely loaded yaml file as Python object.
        """
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def __init__(self):
        params = self.config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
        print("Database connection closed.")
        # TODO change to logging

    def add_new_user(self, user_id, user_data):
        """
        Add a new user to the database using a stored procedure.
        :param user_id: ID of the user to be added to database.
        :param user_data: The data for the corresponding user.
        :return: None.
        """
        self.cur.execute("CALL add_new_user(%s,%s)", (user_id, user_data))
        self.conn.commit()
