init:
	-mkdir audio
	-mkdir logs
	-mkdir transcription
	-mkdir notes

run:
	time python3 main.py

requirements:
	python3 -m pip install -r requirements.txt
