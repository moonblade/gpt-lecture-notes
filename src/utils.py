import os
from src.logger import get_logger

logger = get_logger()
def cleanFileName(fileName):
    directory = os.path.dirname(fileName)
    fileName = os.path.splitext(os.path.basename(fileName))[0]
    fileNameWithUderscores = fileName.replace(" ", "_")
    fileName = os.path.join(directory, fileNameWithUderscores)
    return fileName

def isTranscribed(fileName):
    transcriptionFilePath = os.path.join("transcription", fileName + ".txt")
    exists = os.path.exists(transcriptionFilePath)
    logger.debug(f"{transcriptionFilePath} exists: {exists}")
    return exists

def isMp3File(fileName):
    return fileName.endswith(".mp3")

def isDownloaded(fileName):
    audioFilePath = os.path.join("audio", fileName + ".mp3") 
    exists = os.path.exists(audioFilePath)
    logger.debug(f"{audioFilePath} exists: {exists}")
    return exists
