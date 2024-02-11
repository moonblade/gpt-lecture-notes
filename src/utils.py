import os

def cleanFileName(fileName):
    directory = os.path.dirname(fileName)
    fileName = os.path.splitext(os.path.basename(fileName))[0]
    fileNameWithUderscores = fileName.replace(" ", "_")
    fileName = os.path.join(directory, fileNameWithUderscores)
    return fileName
