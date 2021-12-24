import io
import json

import yaml as yaml
from minio import Minio
from resources import Strings


class ObjectStorage:
    @staticmethod
    def config(
        file_path="C:\\Users\\Luke\\Documents\\projects\\ELT\\local\\load\\s3.yaml",
    ):
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

    def __init__(self):
        """
        Create a connection to a server hosting S3 buckets.
        """
        self.params = self.config()
        self.client = Minio(**self.params)

    def create_bucket(self, bucket_name):
        """
        Create the required bucket if it doesn't already exist.
        :param bucket_name: the name of the desired bucket to create.
        :return: None.
        """
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
        else:
            print(f"Bucket '{bucket_name}' already exists.")
            # TODO change to logging

    def upload_data(self, data, bucket_name, object_name="json"):
        """
        Move json data into an s3 bucket.
        :param data: JSON data to move into bucket.
        :param bucket_name: name of the bucket to upload data into.
        :param object_name: store the object under this name.
        :return: None
        """
        data_stream = io.BytesIO(data)
        data_stream.seek(0)

        self.client.put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            data=data_stream,
            length=len(data),
            content_type="application/json",
        )

    def load_data(self, data):
        """
        Move given data into a MinIO bucket.
        :param data: The data to be stored in a bucket.
        :return: None
        """
        self.create_bucket(Strings.BUCKET_NAME)
        self.upload_data(data, Strings.BUCKET_NAME)

    def get_json_data(self, bucket_name, object_name):
        """
        Get the given json object data from the given bucket.
        :param bucket_name: the name of the bucket to get data from.
        :param object_name: the name of the object to get from the bucket.
        :return: None.
        """
        data = self.client.get_object(bucket_name, object_name)
        json_data = json.loads(json.load(io.BytesIO(data.data)))
        return json_data


def load_data(data):
    """
    Create new S3 object and upload the given data.
    :param data: Data to load into S3 object storage.
    :return: None.
    """
    s3 = ObjectStorage()
    s3.load_data(data)
