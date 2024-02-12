from src.llm import createNotes
from src.logger import get_logger
from src.gdrive import download_file, list_files
from src.transcriber import transcribe
from src.utils import cleanFileName, hasNotes, isDownloaded, isMp3File, isTranscribed


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
                    logger.info(f"Downloading {fileName}")
                    download_file(file["id"], fileName)
                transcribe(fileName)
            if not hasNotes(fileName):
                logger.info(f"Creating notes for {fileName}")
                createNotes(fileName)
                exit()

if __name__ == "__main__":
    main()
