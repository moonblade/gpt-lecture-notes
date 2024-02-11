import os
from src.logger import get_logger
import whisper

from src.utils import getMp3, getTranscription

logger = get_logger()
def transcribe(fileName):
    logger.info(f"Transcribing {getMp3(fileName)}")
    model = whisper.load_model("base")
    result = model.transcribe(getMp3(fileName))
    transcriptionPath = getTranscription(fileName)
    with open(transcriptionPath, "w") as f:
        f.write(str(result))
    logger.info(f"Transcribed to {getTranscription(fileName)}")

