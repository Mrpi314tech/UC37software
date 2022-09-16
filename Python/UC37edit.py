import os
import new_words as aword
import new_com as acom
file_location=os.path.expanduser('~')
print('note: if using quotes, use single quotes')
nwordl=aword.word
ndefl=aword.defi
nwcoml=acom.word
nrunl=acom.com
file_location=os.path.expanduser('~')
qstn=input(" are you adding a command or just words? ")
if 'com' in qstn or 'Com' in qstn:
    kwordc=input("what is the keyword? (what do you want to say to run the command?)")
    outputc=input("what command do you want to run?")
    outc='os.system("'+outputc+'")'
    nwcoml.append(kwordc)
    nrunl.append(outputc)
    file1 = open(file_location+"/UC37software/Python/new_com.py", "w")
    file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
    file1.close()
elif 'wor' in qstn or 'Wor' in qstn:
    kwordw=input("what is the keyword? (what do you want to say so that he says this?)")
    outputw=input("what do you want him to say?")
    nwordl.append(kwordw)
    ndefl.append(outputw)
    file1 = open(file_location+"/UC37software/Python/new_words.py", "w")
    file1.write("word="+str(nwordl)+"\ndefi="+str(ndefl))
    file1.close()
