from minio import Minio
from minio.error import S3Error
import os

def extract_data():
    return None

def transform_data():
    return None

def load_data():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        endpoint="localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    if not client.bucket_exists("dubber"):
        client.make_bucket("dubber")
    else:
        print("Bucket 'dubber' already exists")

    client.fput_object(bucket_name="dubber", object_name="dummy2.txt", file_path=os.path.dirname(os.path.realpath(__file__)) + "\\storage\\dummy2.txt")
    print("Successfully uploaded")

def main():
    extract_data()
    transform_data()
    load_data()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
