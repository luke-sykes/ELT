import logging
import pytest
import yaml
from urllib3.exceptions import MaxRetryError

from local.load.load import LoadS3


class TestLoadS3:

    # TODO delete bucket test after run

    @pytest.fixture
    def create_LoadS3(self):
        obj = LoadS3()
        return obj

    def test_config(self):
        with pytest.raises(FileNotFoundError):
            LoadS3.config(
                file_path="C:\\Users\\Luke\\Documents\\projects\\ELT\\tests\\data\\non_existing_file.yaml"
            )

    def test_create_connection(self, create_LoadS3):
        assert create_LoadS3.client is not None
        try:
            create_LoadS3.client.list_buckets()
        except MaxRetryError:
            logging.critical("Minio Object storage not reachable.")
            assert False

    def test_create_bucket(self, create_LoadS3):
        create_LoadS3.create_bucket("test")
        assert create_LoadS3.client.bucket_exists("test")

    def test_upload_data(self, create_LoadS3):
        # TODO finish writing test
        data = '{"name":"john","age":22,"class":"mca"}'
        create_LoadS3.upload_data(data)
        # assert client.get_object() is not None
