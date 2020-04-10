import os
import requests

def download_file(url, store_path):
    """Download the raw dataset file
    Download the dataset with the given url and save to the store_path
    Args:
        url: the url that can be downloaded the dataset file.
        store_path: the path that stores the downloaded file
    Return:
        the archive format of the suffix
    """
    filename = url.split("/")[-1]
    filepath = os.path.join(store_path, filename)
    print(f'Start downloading file {filename}...')
    file_data = requests.get(url, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)
    print(f'Success loading file {filename} into {filepath}')


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