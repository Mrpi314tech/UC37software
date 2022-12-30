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
    os.system('bla bla bla')
    alias=input('what is the name of the device? ')
    file = open(file_location+"/UC37software/Python/skills/skill_data.py", "w")
    file.write('\nalias="'+alias+'"')
    file.close()
    nameofplug=input('What do you want to call the device?')
    nwcoml.append(nameofplug)
    nrunl.append("python3 "+file_location+"/UC37software/Python/skills/kasa_skill.py")
    file1 = open(file_location+"/UC37software/Python/new_com.py", "w")
    file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
    file1.close()