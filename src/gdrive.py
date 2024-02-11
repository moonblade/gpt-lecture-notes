import urllib.request
from getfilelistpy import getfilelist
from os import path, makedirs, remove, rename
import os
from src.logger import get_logger
from src.utils import getMp3

logger = get_logger()

with open("secrets/googledrive-apikey", "r") as f:
        gdrive_api_key = f.read().strip()

def list_files(remote_folder):
    try:
        resource = {
            "api_key": gdrive_api_key,
            "id": remote_folder.split('/')[-1].split('?')[0],
            "fields": "files(name,id)",
        }
        res = getfilelist.GetFileList(resource)
        return res['fileList'][0]['files']

    except Exception as err:
        logger.exception(err)
        return []


def download_file(remote_file_id, fileName):
    try:
        logger.info(f"Downloading {getMp3(fileName)}")
        source = "https://www.googleapis.com/drive/v3/files/%s?alt=media&key=%s" % (remote_file_id, gdrive_api_key)
        urllib.request.urlretrieve(source, getMp3(fileName))
    except Exception as err:
        logger.exception(err)
        raise
