from src.logger import get_logger
from src.gdrive import list_files
from src.utils import cleanFileName


logger = get_logger()
def main():
    gdriveFolder = "1myOC0YxE5rjbCI-vwe0ZcskNJ-9Tb6IL"
    files = list_files(gdriveFolder)
    for file in files:
        logger.debug(f"Checking {file['name']}")
        fileName = cleanFileName(file["name"])
        exit()

if __name__ == "__main__":
    main()
