import io
import json
from minio import Minio


def transform_data():
    client = Minio(
        endpoint="localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False,
    )
    data = client.get_object("dubber2", "json")
    loaded_data = json.loads(json.load(io.BytesIO(data.data)))
    print(loaded_data)
    transformed_data = loaded_data
    return transformed_data
