import io
import yaml as yaml
from minio import Minio
from resources import Strings


class LoadS3:
    def __init__(self):
        """
        Create a connection to a server hosting S3 buckets.
        """
        self.params = self.config()
        self.client = Minio(**self.params)

    @staticmethod
    def config(
        file_path="C:\\Users\\Luke\\Documents\\projects\\ELT\\local\\load\\s3.yaml",
    ):
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

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

    def upload_data(self, data):
        """
        Move json data into an s3 bucket.
        :param client: client containing the bucket.
        :param data: JSON data to move into bucket.
        :return: None
        """
        data_stream = io.BytesIO(data)
        data_stream.seek(0)

        self.client.put_object(
            bucket_name="dummy-bucket",
            object_name="json",
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
        self.create_bucket(bucket_name=Strings.BUCKET_NAME)
        self.upload_data(data)


def load_data(data):
    """
    Create new S3 object and upload the given data.
    :param data: Data to load into S3 object storage.
    :return: None.
    """
    s3 = LoadS3()
    s3.load_data(data)
