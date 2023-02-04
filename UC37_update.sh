#!/bin/bash
location="$HOME"
mv ~/UC37software/Python/new_words.py ~
mv ~/UC37software/Welcome/info.py ~
mv ~/UC37software/Python/new_com.py ~
mv ~/UC37software/Python/skills ~
echo 'type "y" if it asks you a question: '
rm ~/.local/share/applications/UC37.desktop
rm -r ~/UC37software
git clone https://github.com/Mrpi314tech/UC37software
rm ~/UC37software/Python/new_words.py
rm ~/UC37software/Welcome/info.py
rm ~/skills/install_skills.py
mv ~/UC37software/Python/skills/install_skills.py ~/skills
rm -r ~/UC37software/Python/skills
mv ~/skills ~/UC37software/Python
mv ~/new_words.py ~/UC37software/Python
mv ~/info.py ~/UC37software/Welcome
mv ~/new_com.py ~/UC37software/Python
mv ~/UC37_update.sh ~/delete_this_file-UC37
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
chmod +x ~/UC37software/UC37
chmod +x ~/UC37software/UC37_remove.sh
chmod +x ~/UC37software/UC37_install.sh
echo 'type "y" if it asks you a question: '
rm -r ~/UC37software/.git
chmod +x ~/UC37software/UC37_update.sh
mv ~/UC37software/UC37_update.sh ~
