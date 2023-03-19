#!/bin/bash
location="$HOME"
mv ~/UC37software/Python/new_words.py ~
mv ~/UC37software/Welcome/info.py ~
mv ~/UC37software/Python/new_com.py ~
mv ~/UC37software/Python/skills ~
echo 'type "y" if it asks you a question: '
rm -r ~/UC37software
git clone https://github.com/Mrpi314tech/UC37software
rm ~/UC37software/Python/new_words.py
rm ~/UC37software/Welcome/info.py
rm ~/skills/install_skills.py
mv ~/UC37software/Python/skills/install_skills.py ~/skills
rm -r ~/UC37software/Python/skills
mv ~/skills ~/UC37software/Python
mv ~/new_words.py ~/UC37software/Python
sudo pip install keyboard
sudo apt-get install wmctrl
mv ~/info.py ~/UC37software/Welcome
mv ~/new_com.py ~/UC37software/Python
mv ~/UC37_update.sh ~/delete_this_file-UC37
sudo apt-get install xterm
echo "done"
echo "UC37 is installed!"
echo "The UC37 app can be found in Menu>System Tools>UC37"
chmod +x ~/UC37software/UC37
chmod +x ~/UC37software/UC37_remove.sh
chmod +x ~/UC37software/UC37_install.sh
echo 'type "y" if it asks you a question: '
rm -r ~/UC37software/.git
chmod +x ~/UC37software/UC37_update.sh
mv ~/UC37software/UC37_update.sh ~
