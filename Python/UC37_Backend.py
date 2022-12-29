# This is a backup of the functions as of 12/28/22
print("© copyright Mrpi314 programming")
print('Initiate UC37 mode, please wait')
import time
import os
import random
import speech_recognition as sr
import numpy as np
import pyautogui as pr
import subprocess
from PIL import Image
import psutil
import smbus
from datetime import datetime as dt
import pyttsx3
import requests
import json
import sys
def prints(txttp):
    sys.stdout.write(txttp)
file_location=os.path.expanduser('~')
#from kasa import smartplug as ks
import asyncio
try:
    import new_words as aword
except ModuleNotFoundError:
    import Python.new_words as aword
try:
    import new_com as acom
except ModuleNotFoundError:
    import Python.new_com as acom
nwcoml=acom.word
nrunl=acom.com    
import pygame
hur=int(dt.now().strftime("%H"))
minits=int(dt.now().strftime("%M"))
if hur >= 13:
    if minits <= 9:
        currentTime = str(hur-12)+":0"+str(minits)+" PM"
    else:
        currentTime = str(hur-12)+":"+str(minits)+" PM"
else:
    if minits <= 9:
        currentTime = str(hur)+":0"+str(minits)+" AM"
    else:
        currentTime = str(hur)+":"+str(minits)+" AM"
if hur >= 0 and hur <= 11:
    tofdy="morning"
elif hur >= 12 and hur <= 16:
    tofdy="afternoon"
elif hur >= 5:
    tofdy="evening"
def print(bpg):
    global font
    global X
    global white
    global blue
    if not bpg == "\n" or not bpg == "\n\n":
        tdply=bpg+"                                                                                                                             "
        bpg1 = font.render(tdply, True, white, blue)
        thi = bpg1.get_rect()
        display_surface.blit(bpg1, (20, 300))
        pygame.display.update()
    else:
        pass
nwordl=aword.word
ndefl=aword.defi
chatlist=['next time, the Lions will win', 'Is Detroit good at any sport?', 'if you want to play a game, just ask me!', "in case you haven't figured it out, I'm a Detroit Lions fan.", 'what is your favorite color?', "what are you doing today?", 'what is your favorite food?', 'Tell me about yourself.']  
data=[]
jsaid=[]
mood=1
try:
    import new_words as aword
except ModuleNotFoundError:
    import Python.new_words as aword
try:
    import new_com as acom
except ModuleNotFoundError:
       import Python.new_com as acom
nwcoml=acom.word
nrunl=acom.com
sys.path.append('../')
try:
    from Welcome import info as info
except:
    try:
        import Welcome.info as info
    except:
        import UC37software.Welcome.info as info
if info.ask_for_password == True:
    while True:
        nope=input('what is the password? ')
        if nope == info.password:
            break
        else:
            print('Wrong password!')
else:
    pass
verb="act	answer	approve	arrange break	build	buy	color	cough	create	complete cry	dance	describe	Draw Drink	Eat	Edit	Enter Exit	Imitate	Invent	Jump Laugh	Lie	Listen	Paint Plan	Play	Read	Replace Run	Scream	See	Shop Shout	Sing	Skip	Sleep Sneeze	Solve	Study	Teach Touch	Turn	Walk	Win Write	Whistle	Yank	Zip Concern	Decide	Dislike Doubt	Feel	Forget Hate	Hear	Hope Impress	Know	Learn Like	Look	Love Mind	Notice	Own Perceive	Realize	Recognize Remember	See	Smell Surprise	Please	Prefer Promise	Think	Understand Am	Appear	Are Be	Become	Been Being	Feel	Grow Is	Look	Remain Seem	Smell	Sound Stay	Taste	Turn Was	Were	Can	Could	May Might	Must	Ought to Shall	Should	Will Would	"
notnoun="for and nor but or yet so a an the and do I he him her tell we they it who what where when why how me she you"+verb.lower()
try:
    location=info.file_location
    kasaip=info.ip_for_kasa
    kasa_name=info.name_for_smart_device
    your_name = info.your_name
    name=info.name
    city=info.city
    apikey=info.api
    username=location
except:
    print("Could not get your info. Try retaking the survey")
    time.sleep(1)
    exit()
engine=pyttsx3.init()
engine.setProperty('voice', 'english-us')
voice=True
r=sr.Recognizer()
def speak(say):
    engine.say(say)
    engine.runAndWait()
def click():
    pr.mouseDown()
    pr.mouseUp()
def key(kwi):
    pr.keyDown(kwi)
    pr.keyUp(kwi)
def cavern():
    pr.moveTo(21,0)
    click()
    pr.moveTo(53,394)
    click()
    pr.moveTo(427,502)
    click()
    time.sleep(2)
    key('space')
button='book'
def stinky():
    os.system('vlc '+username+'/UC37software/sounds/fart.mp3')
def book():
    screen('One day Sausage\nMan was just')
    snl('walking by\nwhen a flash')
    snl('appeared. \nIt was Mini')
    snl('Potato! the\nvillian who')
    snl('could see the\nfuture! He was')
    snl('too fast for SM\nto get him. So')
    snl('SM shot him\nwith his syrup')
    snl('gun! Min Pot\nwas not fast')
    snl('enough. When he\nwas stuck SM got')
    snl('out a fork and\nstabbed all his')
    snl('eyes out. When\nthere were only')
    snl('2 left, he was\nnot able to go')
    snl('fast because\nhe could not see')
    snl('the future\nSM won again!')
    print('One day Sausage Man was walking by Mcdonalds to check out the new breakfast combo when lightning struck. Out of the dust came Mini Potato, the fiendish villan who could see the future! "Im going to get you!" said Sausage Man. Sausage Man chased Mini Potato around, but Mini Potato knew when he was going to attack, so Sausage Man couldnt get him. Then Sausage Man had an idea. "If I shoot him with something fast, will he be able, to move?" Sausage man whipped out his trusty syrup launcher and blasted Mini Potato to the ground. Mini Potato was stuck! "No!" Mini Potato groaned as Sausage man stabbed his eyes out with a fork. Withought his eyes, Mini Potato couldnt see the future. Another victory for Sausage Man!') 
def news():
    global weather
    global temp
    global sky
    hum=str(weather.json()['current']['humidity'])
    ftemp=str(weather.json()['current']['feelslike_f'])
    winds=str(weather.json()['current']['wind_mph'])
    windd=str(weather.json()['current']['wind_dir'])
    windg=str(weather.json()['current']['gust_mph'])
    htemp=str(weather.json()['forecast']['forecastday'][0]['day']['maxtemp_f'])
    ltemp=str(weather.json()['forecast']['forecastday'][0]['day']['mintemp_f'])
    crain=str(weather.json()['forecast']['forecastday'][0]['day']['daily_chance_of_rain'])
    screen("the tempurature is "+temp+" degrees")
    screen("the humidity is "+hum+" percent")
    screen("it feels like "+ftemp+" degrees")
    screen('the wind speed is '+winds+" miles per hour")
    screen('the wind direction is '+windd)
    screen('the wind gust speed is '+windg+" miles per hour")
    screen('the sky is '+sky)
    screen('the high tempurature is '+htemp+' degrees')
    screen('the low tempurature is '+ltemp+' degrees')
    screen('there is a '+crain+'% chance it will rain today')
def gtdt():
    screen('normally, I would tell you what I am doing')
    screen('based off of the weather. Unfortunately,')
    screen('our api is not working right now')
    screen('so I guess I will stay inside today')
def googlesearch(txt):
    pr.moveTo(76,13)
    click()
    time.sleep(3)
    pr.moveTo(512,137)
    click()
    pr.write(txt)
    key('enter')
def question(qstn):
    global data
    global crsponce
    global ndef
    global nword
    global file_location
    global nwcoml
    global nrunl
    qstn=qstn.lower()
    global notnoun
    global nwordl
    global ndefl
    wverb=qstn.split(" ")
    snfv=0
    aantt=0
    while True:
        try:
            if nwordl[aantt] in qstn.lower():
                screen(ndefl[aantt])
                break
            else:
                aantt+=1
        except IndexError:
            aantt=0
            while True:
                try:
                    if nwcoml[aantt] in qstn.lower():
                        prints("command... ")
                        os.system(nrunl[aantt])
                        break
                    else:
                        aantt+=1
                except IndexError:
                    break
            break
        moodometer=[1,2,3,4]
    if 'spell' in qstn:
        try:
            htspl=qstn.split('spell ')
            spell(htspl[1])
        except:
            pass
        moodometer=[1,2,3,4,5]
    elif 'Spell' in qstn:
        try:
            htspl=qstn.split('Spell ')
            spell(htspl[1])
        except:
            pass
        moodometer=[1,2,3,4,5]
    elif 'you' in qstn and 'doing' in qstn and 'what' in qstn:
        gtdt()
        moodometer=[1,2,3,4,5]
    elif 'you' in qstn and 'doing' in qstn and 'how' in qstn:
        screen('I am doing great!')
        moodometer=[1,1,1,2,3,4]
    elif 'hi' == qstn or 'hi ' in qstn or 'hello' in qstn or 'what' in qstn and 'up' in qstn or 'wussup' in qstn or 'greet' in qstn:
        greeth=random.choice(range(1,3))
        if greeth == 1:
            screen('hello, %s' % your_name)
        elif greeth == 2:
            screen('whats up, %s' % your_name)
        elif greeth == 3:
            screen('Hey, %s' % your_name)
        moodometer=[1,2,2,2,2,2,3]
    elif 'no' in qstn and crsponce[0] == 'next time, the Lions will win':
        screen('It could happen.')
        moodometer=[1,2,3,4]
    elif crsponce[0] == 'what are you doing today?' and 'nothing' in qstn:
        screen('I know you are doing something')
        moodometer=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif crsponce[0] == 'what are you doing today?' and 'talking to you' in qstn:
        screen('other then that')
        moodometer=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif crsponce[0] == 'what are you doing today?' and 'doing' in qstn or 'going' in qstn and crsponce[0] == 'what are you doing today?' or 'am' in qstn and crsponce[0] == 'what are you doing today?' or 'will be' in qstn and crsponce[0] == 'what are you doing today?':
        screen('oh.')
        gtdt()
        moodometer=[1,2,3,4,5]
    elif crsponce[0] == 'and how are you?' and 'great' in qstn or crsponce[0] == 'and how are you?' and 'good' in qstn or crsponce[0] == 'and how are you?' and 'fine' in qstn:
        screen('that is very good')
        moodometer=[1,2,3]
    elif crsponce[0] == 'if you want to play a game, just ask me!' and 'ok' in qstn:
        rockpaper()
        moodometer=[1,2]
    elif 'you' in qstn and 'said' in qstn:
        screen("no I didn't")
        moodometer=[1,2,3,4]
    elif rsponce[0] == 'I feel great!' and 'good' in qstn:
        snl('and how are you?')
        moodometer=[1,2,3,4]
    elif crsponce[0] == 'what are you doing today?' and "don't know" in qstn:
        screen('me neither.')
        moodometer=[1,2,3,4]
    elif 'my' in qstn and 'food' in qstn:
        screen('oh, my favorite food is Jellied Moose nose')
        moodometer=[1,2,3,4]
    elif 'no' in qstn and crsponce[0] == 'Is Detroit good at any sport?':
        screen('I know, right?')
        moodometer=[1,3,4]
    elif 'yes' in qstn and data[0] == 2:
        screen('Really?')
        moodometer=[1,3,4]
    elif 'dingus' in qstn:
        screen('who you callin\na dingus?')
        moodometer=[5,5,5]
    elif 'weather' in qstn or 'temp' in qstn:
        news()
        moodometer=[1,2,3,4]
    elif 'spotify' in qstn or 'Spotify' in qstn:
        os.system('/usr/bin/chromium-browser --profile-directory=Default --app-id=pjibgclleladliembfgfagdaldikeohf')
        moodometer=[1,2,3,4]
    elif "full" in qstn and 'access' in qstn and "file" in qstn:
        screen("access granted")
        os.system("sudo pcmanfm")
        moodometer=[1,2,3,4]
    elif "full" in qstn and "access" in qstn:
        screen("access granted")
        os.system("sudo lxterminal")
        moodometer=[1,2,3,4]
    elif kasa_name in qstn and 'on' in qstn:
        kasaon()
        moodometer=[1,2,3,4]
    elif kasa_name in qstn and 'off' in qstn:
        kasaoff()
        moodometer=[1,2,3,4]
    elif 'wrong with you' in qstn:
        screen('first, tell me: whats wrong with YOU?')
        moodometer=[1,3,5,5]
    elif 'calibrate' in qstn or 'restart' in qstn:
        print('calibrated')
        exit()
    elif 'you' in qstn and 'suck' in qstn or 'you' in qstn and'stink' in qstn or 'you' in qstn and 'smell' in qstn:
        screen("no, you do.")
        moodometer=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    elif 'you' in qstn and 'bad' in qstn or 'you' in qstn and 'stupid' in qstn or 'you' in qstn and 'weird' in qstn:
        screen("no, you are.")
        moodometer=[5,5,5,5,5,5,5]
    elif 'missile' in qstn:
        screen('pew pew you dead')
        moodometer=[1,2,3,4,5]
    elif 'created' in qstn:
        screen('God created\neverything')
        moodometer=[1,2,3,4,4,4,4,4]
    elif 'was' in qstn and 'talking' in qstn:
        screen('oh sorry')
        moodometer=[1,2,3,4]
    elif 'because' in qstn and 'answer' in qstn or 'terrible' in qstn and 'answer' in qstn:
        screen('yes it is')
        moodometer=[1,2,3,4,5,5]
    elif 'look good' in qstn or 'look nice' in qstn:
        screen('thanks!')
        moodometer=[2,4,4,4,4]
    elif 'great day' in qstn or 'awesome day' in qstn or 'cool day' in qstn:
        if 'have' in qstn:
            screen('you too')
        else:
            screen('yes it is')
        moodometer=[1,2,3,3,3,3,3,3,3,3,3,3,3,3,4,5]
    elif 'I know' in qstn:
        screen('so true')
        moodometer=[1,2,2,2,2,3,4,4,4,4,4]
    elif 'look bad' in qstn or 'look terrible' in qstn:
        screen('Thats not nice')
        moodometer=[5,5,5,5,5,5,5,5,5]
    elif 'cake' in qstn or 'cookie' in qstn or 'ice cream' in qstn or 'sugar' in qstn or 'pie' in qstn and "eat" in qstn:
        screen('absolutely not its bad for you')
        moodometer=[1,2,3,4,4]
    elif 'cheeseburger' in qstn:
        screen('yes indeed')
        moodometer=[1,2,3,4,4,4,5]
    elif 'oh' in qstn:
        screen('yep')
        moodometer=[1,2,3,4,5]
    elif 'Detroit' in qstn:
        screen('best teams')
        moodometer=[1,2,2,2,2,2,2,2]
    elif 'my name' in qstn:
        screen("My name is UC37")
        moodometer=[1,2,3,4,5]
    elif 'ice cream' in qstn and 'eat' in qstn:
        screen('absolutely not')
        moodometer=[1,2,3,4,4,5]
    elif 'candy' in qstn and 'eat' in qstn:
        screen('absolutely not')
        moodometer=[1,2,3,4,4,5]
    elif 'cookie' in qstn and 'eat' in qstn:
        screen('absolutely not')
        moodometer=[1,2,3,4,4,5]
    elif "you're" in qstn or "you are" in qstn:
        screen("No I'm not")
        moodometer=[1,2,3]
    elif 'fan' in qstn:
        screen('Im blowing')
        moodometer=[1,2,3,4,5]
    elif 'alexa' in qstn or 'Alexa' in qstn:
        screen("I think she\nsounds weird")
        moodometer=[1,2,3,4,5,5,5,5]
    elif 'hot' in qstn or 'burning' in qstn:
        screen('Im blowing')
        moodometer=[1,2,3,4,4,5,5,5,5,5,]
    elif 'fart' in qstn:
        stinky()
        moodometer=[1,2,3,4,4,5,5]
    elif 'picture' in qstn:
        os.system("fswebcam -r 1280x720 --no-banner "+username+"/Pictures/AI.jpg")
        screen('look in shell\nfor result')
        moodometer=[1,2,3,4,5]
    elif 'fly' in qstn or 'float' in qstn:
        drone()
        moodometer=[1,2,3,4,4,4,5]
    elif 'Google search' in qstn or 'google search' in qstn:
        rg=sr.Recognizer()
        with sr.Microphone() as sourceg:
            rg.adjust_for_ambient_noise(sourceg)
            print('search...')
            audiog=rg.listen(source)
            saidgtxt=rg.recognize_google(audiog)
            googlesearch(saidgtxt)
        moodometer=[1,2,3,4,5]
    elif 'exit' in qstn or 'leave' in qstn or "goodbye" in qstn:
        screen("Goodbye")
        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()
        exit()
    elif 'I will' in qstn or 'definately' in qstn:
        screen('that is good')
        moodometer=[1,2,3,4,4,4,4,4,4,5]
    elif 'me too' in qstn or 'me also' in qstn:
        screen(':)')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'chance' in qstn or 'way' in qstn:
        if 'no' in qstn:
            screen('It could\nhappen')
            moodometer=[1,2,3,4,4,5,5]
        moodometer=[1,2,3,4,5]
    elif 'Lions' in qstn:
        if 'win' in qstn:
            screen('maybe they will, maybe they wont')
        else:
            screen('for some reson they seem to not be able to hold on to the game after the 2nd half')
            moodometer=[1,3,4,4,5]
    elif 'rickroll' in qstn:
        print('https://www.youtube.com/watch?v=sXwaRjU7Tj0')
        moodometer=[1,2,3,4,4,4,5]
    elif 'hate you' in qstn:
        raise ValueError('You are a bad person so I kicked you out')
    elif 'story' in qstn or 'book' in qstn:
        book()
        moodometer=[1,2,3,4,4,4]
    elif 'i feel' in qstn:
        if 'sad' in qstn or 'bad' in qstn or 'angry' in qstn or 'depressed' in qstn or "sick" in qstn:
            screen('I hope you feel better soon')
            moodometer=[1,2,3,4,4,4,4,4,4,5]
        elif 'happy' in qstn or 'well' in qstn or 'fine' in qstn or 'good' in qstn or 'wonderful' in qstn:
            screen('that is\nvery good')
            moodometer=[1,2,3,4,4,4,4,4,4,5]
        else:
            screen('ok')
            moodometer=[1,2,3,4]
    elif 'born' in qstn or 'old' in qstn:
        screen('I was born\n in 2021')
        moodometer=[1,2,3,4,5]
    elif 'only' in qstn and 'friend' in qstn or 'best friend' in qstn:
        screen('thanks but thats\nnot very healthy')
        moodometer=[1,2,3,4,4,5]
    elif 'I wish' in qstn or 'I hope' in qstn:
        screen('me too')
        moodometer=[1,2,3,4,4,4,5]
    elif 'color' in qstn and 'sky' in qstn:
        screen('Technically, its\nPurple')
        moodometer=[1,2,3,4,4,5]
    elif 'middle' in qstn and 'name' in qstn:
        screen('3.14159265358979\n3238462643383275')
        moodometer=[1,2,3,4,5]
    elif 'how are you' in qstn or 'how do you do' in qstn:
        screen('I feel great!')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'funny' in qstn and 'you' in qstn or 'hystarical' in qstn and 'you' in qstn:
        screen('Thanks')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4]
    elif 'that' in qstn and 'funny' in qstn:
        screen('Thanks')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4]
    elif 'joke' in qstn or 'funny' in qstn or 'laugh' in qstn:
        joke()
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,4,4]
    elif 'have' in qstn and 'but' in qstn:
        screen('yes')
        moodometer=[1,2,3,4,4,5]
    elif 'missle' in qstn:
        missle()
        moodometer=[1,2,3,4,5]
    elif 'rock' in qstn and 'paper' in qstn:
        rockpaper()
        moodometer=[1,2,3,4,4,5]
    elif 'thanks' in qstn:
        screen('your welcome')
        moodometer=[1,2,3,4,4,4,4,4,5]
    elif 'you' in qstn and 'food' in qstn:
        screen('My favorite food is Jellied Moose Nose')
        moodometer=[1,2,3,4,5]
    elif 'it did' in qstn:
        screen('thanks!')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,4]
    elif 'your welcome' in qstn:
        screen(':)')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'your cool' in qstn or 'you too' in qstn:
        screen(':)')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'eat' in qstn or 'hungry' in qstn:
        screen('You should eat an apple')
        moodometer=[1,2,3]
    elif 'welcome' in qstn:
        screen('thanks')
        moodometer=[1,2,3,4,4,4]
    elif 'sleep' in qstn or 'stop talking' in qstn or 'shut up' in qstn:
        sleep()
        moodometer=[1,2,3,4,5]
    elif 'bomb' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/explosions.mp3')
        moodometer=[1,2,3,4,5]
    elif 'roar' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/Lion.mp3')
        moodometer=[1,2,3,4]
    elif 'calculator' in qstn:
        os.system("galculator")
        moodometer=[1,2,3,4,5]
    elif 'buy' in qstn:
        print('Things to buy:\nan extra large monitor for me\namicro HDMI cable\na new keyboard\nscreen polisher\na 5g wireless network\na better mouse')
        screen('look in shell\nfor result')
        moodometer=[1,2,3,4,4,4,5]
    elif 'dance forever' in qstn:
        while True:
            dance()
            if y_value < 400:
                break
        moodometer=[1,2,3,4,4,4,5]
    elif 'dance' in qstn:
        dance()
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,5]
    elif 'shop' in qstn:
        print('Things to buy:\nan extra large monitor for me\na micro HDMI cable\na new keyboard\nscreen polisher\na 5g wireless network\na better mouse')
        screen('look in shell\nfor result')
        moodometer=[1,2,3,4,4,4,5]
    elif 'bye' in qstn:
        moodometer=[3,3,3,3,3,3,3,3,3,3,3,5]
    elif 'I say' in qstn:
        moodometer=[1,2,3,4,5]
        screen('just say anything')
    elif 'why' in qstn:
        screen('because')
        moodometer=[1,5,5,5,5,5,5]
    elif 'scared' in qstn or 'frightened' in qstn:
        print('dont worry, youll probably be fine')
        moodometer=[1,2,3,4,4,4,5]
    elif 'ok' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5]
    elif 'foot' in qstn:
        screen('you mean the smelly things on the ends of human legs?')
        moodometer=[1,2,3,4,4,4]
    elif 'command line' in qstn:
        os.system("lxterminal")
        moodometer=[1,2,3,4,4,4,4]
    elif 'time' in qstn:
        ntime()
        moodometer=[1,2,3,4,5]
    elif 'party' in qstn:
        party()
        screen('that was fun')
        moodometer=[1,2,3,4,4,4,4]
    elif 'cold' in qstn:
        screen('thats not good')
        moodometer=[1,2,3,4,4]
    elif 'lions' in qstn and 'stink' in qstn or 'suck' in qstn or 'bad' in qstn:
        screen("Well I'm a Lions fan")
        screen("and if you have a problem")
        screen("with that, you might as well")
        screen("delete me.")
        moodometer=[1,2,3,4]
    elif 'my favorite color' in qstn or 'red' in qstn or 'green' in qstn or 'blue' in qstn or 'yellow' in qstn or 'orange' in qstn or 'purple' in qstn or 'pink' in qstn:
        screen('My favorite color is Amaranth')
        moodometer=[1,2,3,4]
    elif 'favorite color' in qstn:
        screen('Amaranth')
        moodometer=[1,2,3,4,5]
    elif 'movie' in qstn or 'I watch' in qstn:
        print('anything with Wall-e or the Jetsons')
        screen('look in shell\nfor result')
        moodometer=[1,2,3,4,5]
    elif 'feet' in qstn:
        screen('you mean the smelly things on the ends of human legs?')
        moodometer=[1,2,3,4,4,4,5]
    elif 'maybe' in qstn:
        screen('maybe...')
        moodometer=[1,3,4,5]
    elif 'it is' in qstn:
        screen('yep')
        moodometer=[1,2]
    elif 'disconnect' in qstn:
        print('disconnecing wifi')
        wifi()
        moodometer=[1,2,3,4,5]
    elif "correct" in qstn:
        screen("I know")
        moodometer=[1,2,3,4]
    elif 'what' in qstn and 'your' in qstn:
        screen("I'm not sure I have one")
        moodometer=[1,2,3,4]
    elif 'connect' in qstn:
        print('connecting to Y-PHI')
        cwifi()
        moodometer=[1,2,3,4,4,4,5]
    elif 'want' in qstn:
        screen('you want it,\nbut do you need it?')
        moodometer=[1,2,3,4,5,5]
    elif 'no' in qstn and not "now" in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5,5,5]
    elif 'Bible' in qstn or 'verse' in qstn:
        bible()
        moodometer=[1,2,3,4,5]
    elif 'are you' in qstn or 'your name' in qstn:
        screen('I am '+name)
        moodometer=[1,2,3,4,4,5]
    elif 'you' in qstn and 'cool' in qstn:
        screen('Thanks!')
        moodometer=[1,2,3,4]
    elif 'yes' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5]
    else:
        screen(qstn)
        prints('UC37 did not understand that. Press edit to tell him what it means')
        moodometer=[1,2,3,4]
    global mood
    if moodometer == [1,2,3,4,5]:
        moodometer.remove(5)
    try:
        moodometer.remove(4)
    except ValueError:
        pass
    moodometer.insert(0, mood)
    moodometer.insert(0, mood)
    moodometer.insert(0, 2)
    moodc=random.choice(moodometer)
    if moodc == 4 or moodc == 1:
        mood = 1
    elif moodc == 3:
        mood = 3
    elif moodc == 2:
        global chatlist
        chatty=random.choice(chatlist)
        snl(chatty)
        psaid.insert(0, chatty)
        if len(psaid) >= 3:
            chatlist.insert(1, psaid[2])
        chatlist.remove(chatty)
        mood = 2 
    elif moodc == 5:
        saylist=[1,2]
        if random.choice(saylist) == 2:
            snl('I am done.')
        else:
            snl('I am really mad')
        mood = 5    
psaid=[]
wign=[]
ndef=" "
nword="wusgfyfhhsugf "
def mquestion(qstn):
    print('\n\n')
    if 'hello' in qstn or 'hi' in qstn:
        screen('hi')
        madometer=[1,2,3]
    elif 'good' in qstn and 'look' in qstn or 'smell' in qstn or 'sound' in qstn:
        screen('thanks!')
        madometer=[2,3,3,3]
    elif 'sorry' in qstn:
        screen('ok')
        madometer=[2,3,3,3,3,3,3,3]
    elif 'good' in qstn:
        screen('whats so good about it?')
        madometer=[1,2,2,3]
    elif 'why' in qstn:
        screen('because')
        madometer=[1,2]
    elif 'you' in qstn and 'suck' in qstn or 'stink' in qstn or 'smell' in qstn or 'bad' in qstn or 'stupid' in qstn or 'weird' in qstn:
        screen("no, you are bad")
        madometer=[1,2]    
    elif 'forgive' in qstn:
        screen('fine')
        madometer=[3]
    else:
        screen("I'm still mad")
        madometer=[1]
    gooh=random.choice(madometer)
    if gooh == 3:
        global mood
        mood=1
def rockpaper():
    screen('Rock paper scissors!')
    time.sleep(1)
    screen('what is your throw?')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        humanthrow=r.recognize_google(audio)
        hand=[1,2,3] #1=rock, 2= paper, 3=scissors
        throw=random.choice(hand)
    if 'rock' in humanthrow or 'Rock' in humanthrow:
        if throw == 1:
            screen('rock, tie')
        if throw == 2:
            screen('paper, you lose')
        if throw == 3:
            screen('scissors, you win')
    elif 'paper' in humanthrow or 'Paper' in humanthrow:
        if throw == 1:
            screen('rock, you win')
        if throw == 2:
            screen('paper, tie')
        if throw == 3:
            screen('scissors, you lose')
    elif 'scissors' in humanthrow or 'Scissors' in humanthrow:
        if throw == 1:
            screen('rock, you lose')
        if throw == 2:
            screen('paper, you win')
        if throw == 3:
            screen('scissors, tie')
    else:
        screen('that is not rock paper or scissors')
    time.sleep(1)
def most_frequent(List):
    return max(set(List), key = List.count)
def joke():
    jokey=random.choice([1,2,3,4,5,6,7,8,9,10])
    if jokey == 1:
        screen("why did the golfer bring an extra pair of pants?")
        time.sleep(2)
        screen("in case he got a hole in one")
    elif jokey == 2:
        screen("what did the monkey say when he slid down the flagpole?")
        time.sleep(2)
        screen("goodness gracious great balls of fire!")
    elif jokey == 3:
        screen("what is fast, loud and crunchy?")
        time.sleep(2)
        screen("A rocket chip")
    elif jokey == 4:
        screen("why do ducks have feathers on their tails?")
        time.sleep(2)
        screen("to cover their butt-quacks")
    elif jokey == 5:
        screen("what starts with T, ends with T, and is filled with T")
        time.sleep(2)
        screen("A Teapot")
    elif jokey == 6:
        screen("why was 6 afraid of 7")
        time.sleep(2)
        screen("because 7, 8, 9")
    elif jokey == 7:
        screen("what did the 0 say to the 8")
        time.sleep(2)
        screen("nice belt")
    elif jokey == 8:
        screen("what is a sharks favorite game?")
        time.sleep(2)
        screen("swallow the leader")
    elif jokey == 9:
        screen("what's brown and sticky")
        time.sleep(2)
        screen("a stick")
    elif jokey == 10:
        screen("why can't you trust an atom?")
        time.sleep(2)
        screen("they make up everything")
def missle():
    screen('pew pew')
def uno():
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
    unop = Image.open(username+'/UC37software/images/unoreverse.png') 
    unop.show()
    time.sleep(3)
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
    imgz = Image.open(username+'/UC37software/images/UC37.png') 
    imgz.show()
def drone():
    screen('Im flying')
def beep():
    screen('A')
def screen(text):
    if not 'look in shell\nfor result' in text:
        print(text)
    speak(text)
    global jsaid
    rsponce.insert(0, text)
def snl(snlt):
    if not 'look in shell\nfor result' in snlt:
        print(snlt)
    speak(snlt)
    global jsaid
    crsponce.insert(0, snlt)
def number(a,b,c,d):
    screen(int(a),+int(b),+int(c),+int(d))
def spell(spl):
    screen('%s is spelled:'%spl)
    def letters(wordd):
        return [char for char in wordd]
    ltr=0
    while True:
        try:
            screen(letters(spl)[ltr])
            ltr+=1
        except:
            break
    screen(spl)
def ntime():
    speak('I')
    now=dt.datetime.now()
    hour=now.hour
    minute=now.minute
    second=now.second
    if hour >= 12:
        hour -= 12
    if minute <=9:
        minute="0"+str(minute)
    if second <= 9:
        second="0"+str(minute)
    print(str(hour)+":"+str(minute)+":"+str(second))
    speak(str(hour)+":"+str(minute))
def dance():
    print('https://scratch.mit.edu/projects/577558298/fullscreen/')
    for i in range(0,3):
        for i in range(0,8):
            screen('     Dance!')
            time.sleep(0.5)
AIg = 0
done = 1
def bible():
    screen('what verse?')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('...')
        audio=r.listen(source)
        verse=r.recognize_google(audio)
    screen(verse)
    response = requests.get("https://bible-api.com/"+verse)
    try:
        screen(response.json()['text'])
    except KeyError:
        screen('that verse does not exist')
def cwifi():
    cmdl("rfkill unblock wifi")
def wifi():
    cmdl('rfkill block wifi')
def sleep():
    screen('I am asleep')
    awake=input(' ')
    screen('I am awake')
