#just click the run button and wait for things to download
from subprocess import call
import os
call(["pip3","install","SpeechRecognition"])
call(["sudo","apt-get","install","flac"])
call(["pip3","install","pyautogui"])
call(["pip3","install","pyttsx3"])
call(["sudo","apt","install","espeak"])
os.system("sudo pip install pyaudio")
os.system("sudo apt install fswebcam")
os.system("sudo pip install python-kasa")
print('this is your smartplug info:')
os.system('kasa')
import Survey