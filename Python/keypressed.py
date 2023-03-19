#sudo python3 ~/UC37software/Python/keypressed.py
import keyboard
import os
file_location=os.path.expanduser('~')
def hotkey(event):
    if event.name == 'f10':
        os.system("window_id=$(wmctrl -l | grep 'UC37software' | awk '{print $1}') && wmctrl -i -a $window_id")
keyboard.on_press(hotkey)
keyboard.wait()

