import os
import requests
from beta_rec.utils.onedrive import OneDrive

def download_file(url, store_file_path):
    """Download the raw dataset file

    Download the dataset with the given url and save to the store_path
    Args:
        url: the url that can be downloaded the dataset file.
        store_path: the path that stores the downloaded file
    Return:
        the archive format of the suffix
    """
    filename = url.split("/")[-1]
    print(f'Start downloading file {filename}...')
    file_data = requests.get(url, allow_redirects=True).content
    with open(store_file_path, 'wb') as handler:
        handler.write(file_data)
    print(f'Success loading file {filename} to {store_file_path}')


def get_format(suffix):
    """ Get the archive format

    Get the archive format of the archive file with its suffix
    Args:
        suffix: suffix of the archive file
    Return:
        the archive format of the suffix
    """
    format_map = {
        'bz2': 'bztar',
    }
    if suffix not in format_map:
        return suffix
    return format_map[suffix]


def download_file_from_onedrive(url, path):
    folder = OneDrive(url=url, path=path)
    folder.download()
