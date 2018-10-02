import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"


def get_fremont_data(filename="Fremont.csv", url=FREMONT_URL,
                     force_download=False):
    """Download and cache the Fremont data

    Args:
        filename (str): location to save the data
        url (str): web location of the data
        force_download (bool): if True, re-download data

    Returns:
        pandas.DataFrame: the Fremont bridge data.

    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv(filename, index_col="Date", parse_dates=True)
    data.columns = ["East", "West"]
    data["Total"] = data["West"] + data["East"]
    return data
