import urllib.request
from getfilelistpy import getfilelist
from os import path, makedirs, remove, rename
import logging
import os

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
        logging.exception(err)
        return []


def download_file(remote_file_id, fileName):
    try:
        source = "https://www.googleapis.com/drive/v3/files/%s?alt=media&key=%s" % (remote_file_id, gdrive_api_key)
        urllib.request.urlretrieve(source, os.path.join("audio", fileName + ".mp3"))

    except Exception as err:
        print(err)

