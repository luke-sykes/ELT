from load.load import ObjectStorage
from resources import Strings


def transform_data():
    """Transform the given data

    Perform operations on given data to produce transformed data set.

    :return: The transformed data.
    :rtype:
    """
    s3 = ObjectStorage()
    data = s3.get_json_data(bucket_name=Strings.BUCKET_NAME, object_name="json")
    print(data)
    return data
