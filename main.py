from src.logger import get_logger
from src.gdrive import download_file, list_files
from src.utils import cleanFileName, isDownloaded, isMp3File, isTranscribed


logger = get_logger()
def main():
    gdriveFolder = "1myOC0YxE5rjbCI-vwe0ZcskNJ-9Tb6IL"
    files = list_files(gdriveFolder)
    for file in files:
        if isMp3File(file["name"]):
            fileName = cleanFileName(file["name"])
            logger.debug(f"Checking {fileName}")
            if not isTranscribed(fileName):
                if not isDownloaded(fileName):
                    logger.debug(f"Downloading {fileName}")
                    download_file(file["id"], fileName)
            exit()

if __name__ == "__main__":
    main()
