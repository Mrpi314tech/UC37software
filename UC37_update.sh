#!/bin/bash
mv ~/UC37software/Python/new_words.py ~
mv ~/UC37software/Welcome/info.py ~
rm -r ~/UC37software
git clone https://github.com/Mrpi314tech/UC37software
rm ~/UC37software/Python/new_words.py
rm ~/UC37software/Welcome/info.py
mv ~/new_words.py ~/UC37software/Python
mv ~/info.py ~/UC37software/Welcome
rm ~/UC37software/UC37_update.sh
chmod +x ~/UC37software/UC37
chmod +x ~/UC37software/UC37_remove.sh
chmod +x ~/UC37software/UC37_install.sh
