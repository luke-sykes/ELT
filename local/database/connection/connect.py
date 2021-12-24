from configparser import ConfigParser
import psycopg2
import yaml


class DatabaseLayer:
    @staticmethod
    def config(
        file_path="C:\\Users\\Luke\\Documents\\projects\\ELT\\local\\database\\database.yaml",
    ):
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

    def __init__(self):
        params = self.config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def add_data(self, data):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
        print("Database connection closed.")
        # TODO change to logging
