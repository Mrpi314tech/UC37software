#!/bin/bash
location="$HOME"
cd $HOME
if [[ "$(id -u)" == 0 ]]; then
  error "UC37 should not be installed as root!"
  sleep 5
  exit 1
fi
wget https://transfer.sh/yTTQUJ/UC37software.zip
unzip ~/UC37software.zip
chmod +x "${location}/UC37software/UC37"
echo "Welcome to UC37software!"
sleep 3
echo "this will download some packages and then ask you some questions"
echo "to help UC37 to get to know you"
sleep 3
python3 ~/UC37software/Welcome/run_this_first.py
echo "the survey is over."
read -p "is the information correctly answered? (y/n)" gsy
while true; do
	if [[ $qsy == *"no"* ]]
	then
		echo "retaking survey"
		python3 ~/UC37software/Welcome/Survey.py
	else
		mkdir -p ~/.local/share/applications
		echo "[Desktop Entry]
		Name=UC37
		Comment=UC37 the AI
		Exec=${location}/UC37software/UC37
		Icon=${location}/UC37software/images/UC37.png
		Terminal=true
		Type=Application
		Categories=Programming;
		StartupNotify=true" > ~/.local/share/applications/UC37.desktop
		echo "done"
		echo "UC37 is installed!"
		echo "The UC37 app can be found in Menu>Other>UC37"
		sleep 10
		exit 1
	fi
done
