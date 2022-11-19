#!/bin/bash
mv ~/UC37software/Python/new_words.py ~
mv ~/UC37software/Welcome/info.py ~
mv ~/UC37software/Python/new_com.py ~
echo 'type "y" for the next 5 questions: '
rm -r ~/UC37software
git clone https://github.com/Mrpi314tech/UC37software
rm ~/UC37software/Python/new_words.py
rm ~/UC37software/Welcome/info.py
mv ~/new_words.py ~/UC37software/Python
mv ~/info.py ~/UC37software/Welcome
mv ~/new_com.py ~/UC37software/Python
mv ~/UC37_update.sh ~/delete_this_file-UC37
chmod +x ~/UC37software/UC37
chmod +x ~/UC37software/UC37_remove.sh
chmod +x ~/UC37software/UC37_install.sh
echo 'type "y" for the next 2 questions: '
rm -r ~/UC37software/.git
chmod +x ~/UC37software/UC37_update.sh
mv ~/UC37software/UC37_update.sh ~
mv ~/UC37_update.sh ~/delete_this_file-UC37
