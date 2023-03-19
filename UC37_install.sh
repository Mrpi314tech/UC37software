#!/bin/bash
chmod +x ~/UC37software/UC37_install
location="$HOME"
cd $HOME
if [[ "$(id -u)" == 0 ]]; then
  error "UC37 should not be installed as root!"
  sleep 5
  exit 1
fi
chmod +x "${location}/UC37software/UC37"
chmod +x "${location}/UC37software/UC37_remove.sh"
mv ~/UC37software/UC37_update.sh ~
chmod +x "${location}/UC37_update.sh"
echo "Welcome to UC37software!"
sleep 3
echo "this will download some packages"
sleep 3
pip3 install SpeechRecognition
pip install numpy
sudo apt-get install flac
pip3 install pyautogui
sudo apt-get install python3-tk python3-dev
sudo apt install espeak
sudo apt-get install portaudio19-dev
sudo apt-get install xterm
sudo pip install pyaudio
pip install pillow
sudo apt-get install alsa-utils
pip install pygame
pip install psutil
pip install smbus
pip install pyttsx3
pip install keyboard
sudo apt-get install wmctrl
sudo apt install fswebcam
sudo apt-get install htop
echo 'type "y" if it asks you a question: '
rm -r ~/UC37software/.git
echo "Now you will take a survey to help UC37 get to know you"
sleep 3
python3 ~/UC37software/Welcome/Survey.py
echo "the survey is over."
read -p "is the information correctly answered? (y/n)" gsy
while true; do
	if [[ $qsy == *"n"* ]]
	then
		echo "retaking survey"
		python3 ~/UC37software/Welcome/Survey.py
	else
		echo "#!/bin/bash
		~/UC37software/UC37"' "$@"' | sudo tee /usr/local/bin/UC37 -p /usr/local/bin
		sudo chmod +x /usr/local/bin/UC37
		mkdir -p ~/.local/share/applications
		echo "[Desktop Entry]
		Name=UC37
		Comment=UC37 the AI
		Exec=UC37
		Icon=${location}/UC37software/images/UC37.png
		Terminal=false
		Type=Application
		Categories=System;
		StartupNotify=true" > ~/.local/share/applications/UC37.desktop
		echo "done"
		echo "UC37 is installed!"
		echo "The UC37 app can be found in Menu>System Tools>UC37"
		sleep 10
		exit 1
	fi
done
