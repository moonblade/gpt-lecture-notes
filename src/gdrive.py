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


def download_googledrive_folder(remote_folder, local_dir):
    try:
        resource = {
            "api_key": gdrive_api_key,
            "id": remote_folder.split('/')[-1].split('?')[0],
            "fields": "files(name,id)",
        }
        res = getfilelist.GetFileList(resource)
        print('Found #%d files' % res['totalNumberOfFiles'])
        destination = local_dir
        if not path.exists(destination):
            makedirs(destination)
        for file_dict in res['fileList'][0]['files']:
            print('Downloading %s' % file_dict['name'])
            # if gdrive_api_key:
            #     source = "https://www.googleapis.com/drive/v3/files/%s?alt=media&key=%s" % (file_dict['id'], gdrive_api_key)
            # else:
            #     source = "https://drive.google.com/uc?id=%s&export=download" % file_dict['id']  # only works for small files (<100MB)
            # destination_file = path.join(destination, file_dict['name'])
            # urllib.request.urlretrieve(source, destination_file)

    except Exception as err:
        print(err)

