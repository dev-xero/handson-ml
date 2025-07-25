import os
import tarfile
import pandas as pd
import numpy as np

from urllib import request
from pathlib import Path
from zlib import crc32

HOUSING_PATH = os.path.join("datasets", "housing")
EXTRACT_PATH = os.path.join(Path(__file__).parents[1], HOUSING_PATH)


def download_housing_data(housing_url, housing_path=EXTRACT_PATH):
    if not os.path.isdir(EXTRACT_PATH):
        os.makedirs(housing_path, exist_ok=True)
        tgz_path = os.path.join(housing_path, "housing.tgz")
        request.urlretrieve(housing_url, tgz_path)
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_path)
        housing_tgz.close()


def load_housing_data(housing_path=EXTRACT_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    # assume test set size is N
    # select first N entries
    test_indices = shuffled_indices[:test_set_size]
    # select other half for training
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32


def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]
