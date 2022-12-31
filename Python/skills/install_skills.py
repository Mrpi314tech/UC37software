import os
import sys
sys.path.append('../')
import new_com as acom
nwcoml=acom.word
nrunl=acom.com
file_location=os.path.expanduser('~')
qstn=input('what skill are you adding?')
if 'kasa' in qstn:
    print('You will need to install the python-kasa library with pip')
    os.system('wget https://raw.githubusercontent.com/Mrpi314tech/UC37skills/main/kasa_skills.py ~/UC37software/Python/skills')
    alias=input('what is the name of the device? ')
    file = open(file_location+"/UC37software/Python/skills/skill_data.py", "a")
    file.write('\nalias="'+alias+'"')
    file.close()
    nameofplug=input('What do you want to call the device?')
    nwcoml.append(nameofplug)
    nrunl.append("python3 "+file_location+"/UC37software/Python/skills/kasa_skill.py")
    file1 = open(file_location+"/UC37software/Python/new_com.py", "w")
    file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
    file1.close()
elif 'timer' in qstn:
    os.system('wget https://raw.githubusercontent.com/Mrpi314tech/UC37skills/main/timer.py ~/UC37software/Python/skills')
    ringer=input('what mp3 file do you want to play when the timer is over? ')
    file = open(file_location+"/UC37software/Python/skills/skill_data.py", "a")
    file.write('\nringer="'+ringer+'"')
    file.close()
    nwcoml.append('timer')
    nrunl.append("lxterminal -e python3 "+file_location+"/UC37software/Python/skills/timer.py")
    file1 = open(file_location+"/UC37software/Python/new_com.py", "w")
    file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
    file1.close()
