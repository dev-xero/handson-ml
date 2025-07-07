import os
import tarfile
import pandas as pd

from urllib import request
from pathlib import Path

HOUSING_PATH = os.path.join("datasets", "housing")
EXTRACT_PATH = os.path.join(Path(__file__).parents[1], HOUSING_PATH)


def download_housing_data(housing_url, housing_path=EXTRACT_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=EXTRACT_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)
