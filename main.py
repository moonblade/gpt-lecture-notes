from src.logger import get_logger
from src.gdrive import list_files


logger = get_logger()
def main():
    gdriveFolder = "1myOC0YxE5rjbCI-vwe0ZcskNJ-9Tb6IL"
    files = list_files(gdriveFolder)
    logger.debug(files)

if __name__ == "__main__":
    main()
