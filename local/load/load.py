import io
import json
import yaml as yaml
from minio import Minio
from local.resources import Strings


class ObjectStorage:
    @staticmethod
    def config(
        file_path=Strings.MINIO_CONFIG,
    ):
        """Read a yaml file

        Wrapper function to safely read a yaml file containing the S3 connection configuration.

        :param file_path: location of the configuration file
        :return: A yaml file stream as a Python object
        :rtype: File stream Python object
        """
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

    def __init__(self):
        """Constructor method creates connection to S3 server."""
        self.params = self.config()
        self.client = Minio(**self.params)

    def create_bucket(self, bucket_name):
        """Create a bucket

        Create the required bucket if it doesn't already exist.

        :param bucket_name: the name of the desired bucket to create
        :type: bucket_name: string, required
        """
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
        else:
            print(Strings.BUCKET_NAME.format(bucket_name))
            # TODO change to logging

    def upload_data(self, data, bucket_name, object_name):
        """Move json data into an S3 bucket

        Upload the given data into the given S3 bucket as the given name.

        :param data: JSON data to move into bucket
        :type: data: JSON formatted string, required
        :param bucket_name: name of the bucket to upload data into
        :type: bucket_name: string, required
        :param object_name: store the object under this name
        :type object_name: string, required
        """
        data_stream = io.BytesIO(data)
        data_stream.seek(0)

        self.client.put_object(
            bucket_name=bucket_name,
            object_name=object_name,
            data=data_stream,
            length=len(data),
            content_type=Strings.CONTENT_TYPE,
        )

    def load_data(self, data):
        """Move given data into a MinIO bucket

        Check/create the bucket exists, then load the given data into the bucket

        :param data: The data to be stored in a bucket
        :type data: JSON formatted string, required
        """
        self.create_bucket(Strings.BUCKET_NAME)
        self.upload_data(data, Strings.BUCKET_NAME, Strings.OBJECT_NAME)

    def get_json_data(self, bucket_name, object_name):
        """Get JSON data from a bucket

        Get the given object data from the given bucket as a json Python Object.

        :param bucket_name: the name of the bucket to get data from
        :type: bucket_name: string, required
        :param object_name: the name of the object to get from the bucket
        :type: object_name: string, required
        :return: A Python object containing json data stored in S3
        :rtype: Python Object
        """
        data = self.client.get_object(bucket_name, object_name)
        return json.loads(json.load(io.BytesIO(data.data)))


def load_data(data):
    """Load the data into S3 storage

    Pipeline function called from main to create a new S3 object and upload the given data.

    :param data: Data to load into S3 object storage
    :type: data: JSON formatted string
    """
    S3 = ObjectStorage()
    S3.load_data(data)
