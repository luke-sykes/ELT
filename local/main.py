from local.database.store import store_data
from local.extract.extract import extract_data
from local.load.load import load_data
from local.transform.transform import transform_data


def main():
    """
    Execute the data pipeline.

    :return: None
    """
    data = extract_data()
    load_data(data)


    transform_data()
    store_data()




if __name__ == "__main__":
    main()
