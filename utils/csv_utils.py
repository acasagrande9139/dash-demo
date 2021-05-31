from pathlib import Path

import pandas as pd

# DIR_PATH = "\\\\Mac\\Home\\Documents\\GitHub\\dash-demo\\data"
DIR_PATH = "/Users/acasagrande/Documents/GitHub/dash-demo/data"
EXT_PATH = "**/*.csv"


def get_files():
    return list(Path(DIR_PATH).glob(EXT_PATH))


def get_data(file_path):
    tmp_df = pd.read_csv(file_path)
    return tmp_df


if __name__ == "__main__":
    pass
