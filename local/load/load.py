import io
from minio import Minio


def load_data(data):
    """
    Move given data into a MinIO bucket.
    :param data: The data to be stored in a bucket.
    :return: None
    """
    # TODO move into .ini configuration file
    client = Minio(
        endpoint="localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False,
    )

    if not client.bucket_exists("dubber2"):
        client.make_bucket("dubber2")
    else:
        print("Bucket 'dubber2' already exists")

    data_stream = io.BytesIO(data)
    data_stream.seek(0)

    client.put_object(
        bucket_name="dubber2",
        object_name="json",
        data=data_stream,
        length=len(data),
        content_type="application/json",
    )
    print("Successfully uploaded")
