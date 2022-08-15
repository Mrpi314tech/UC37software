print("© copyright Mrpi314 programming")
print('Initiate UC37 mode, please wait')
import time
import os
import random
import speech_recognition as sr
import numpy as np
import pyautogui as pr
from subprocess import call
from PIL import Image
import psutil
import smbus
import datetime as dt
import pyttsx3
import requests
import json
import sys
from kasa import smartplug as ks
import asyncio
chatlist=['next time, the Lions will win', 'Is Detroit good at any sport?', 'if you want to play a game, just ask me!', "in case you haven't figured it out, I'm a Lions fan.", 'what is your favorite color?', "what are you doing today?", 'what is your favorite food?', 'Tell me about yourself.']  
data=[]
jsaid=[]
mood=1
sys.path.append('../')
try:
    from Welcome import info
except:
    try:
        import version.Python.Windows.info
    except:
        import UC37software.version.Python.Windows.info
if info.ask_for_password == True:
    while True:
        nope=input('what is the password? ')
        if nope == info.password:
            break
        else:
            print('Wrong password!')
else:
    pass
location=info.file_location
kasaip=info.ip_for_kasa
kasa_name=info.name_for_smart_device
your_name = info.your_name
name=info.name
city=info.city
username=location
engine=pyttsx3.init()
engine.setProperty('voice', 'english-us')
voice=True
img = Image.open(username+'/UC37software/images/UC37.png') 
img.show()
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
rfid = False
print('Im taking a picture of you')
os.system("fswebcam -r 1280x720 --no-banner "+username+"/Pictures/secure.jpg")
def stinky():
    screen('stealth farts')
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
    weather = requests.get("http://api.weatherapi.com/v1/forecast.json?key=47fd44846a1248db90e200817221707&q="+city+"&days=1&aqi=no&alerts=no")
    temp=str(weather.json()['current']['temp_f'])
    hum=str(weather.json()['current']['humidity'])
    ftemp=str(weather.json()['current']['feelslike_f'])
    winds=str(weather.json()['current']['wind_mph'])
    windd=str(weather.json()['current']['wind_dir'])
    windg=str(weather.json()['current']['gust_mph'])
    sky=str(weather.json()['current']['condition']['text'])
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
    weather = requests.get("http://api.weatherapi.com/v1/forecast.json?key=47fd44846a1248db90e200817221707&q="+city+"&days=1&aqi=no&alerts=no")
    sky=str(weather.json()['current']['condition']['text'])
    temp=weather.json()['current']['temp_f']
    if 'rain' in sky or 'Rain' in sky:
        screen('it is raining so I guess I will just be watching TV')
    else:
        if temp >= 80:
            screen('It is pretty hot so I will be at the pool')
        elif temp >= 40:
            screen('it is a good day for sports so thats what I will do')
        else:
            screen('it is to cold for me so I will stay inside')
def googlesearch(txt):
    pr.moveTo(76,13)
    click()
    time.sleep(3)
    pr.moveTo(512,137)
    click()
    pr.write(txt)
    key('enter')
def question(qstn):
    print('\n\n')
    global data
    global crsponce
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
    elif crsponce[0] == 'what are you doing today?' and 'doing' in qstn or 'going' and crsponce[0] == 'what are you doing today?' or 'am' in qstn and crsponce[0] == 'what are you doing today?':
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
        GPIO.output(fart, GPIO.LOW)
        GPIO.output(fart2, GPIO.LOW)
        GPIO.output(story1, GPIO.LOW)
        GPIO.output(story2, GPIO.LOW)
        GPIO.output(story3, GPIO.LOW)
        GPIO.output(loud2, GPIO.LOW)
        GPIO.output(loud1, GPIO.LOW)
        lcd.clear()
        lcd.set_backlight(1)
        segment.clear()      
        segment.write_display()
        print('calibrated')
        exit()
    elif 'you' in qstn and 'suck' in qstn or 'stink' in qstn or 'smell' in qstn or 'bad' in qstn or 'stupid' in qstn or 'weird' in qstn:
        screen("no, "+qstn)
        moodometer=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    elif 'romantic' in qstn or 'romance' in qstn or 'love' in qstn or 'careless whisper' in qstn:
        screen('Ooh Lah Lah')
        os.system('vlc /home/mrpi314/UC37software/sounds/Careless_whisper.mp3')
        moodometer=[1,2,3,4]
    elif 'missile' in qstn:
        screen('pew pew you dead')
        moodometer=[1,2,3,4,5]
    elif 'created' in qstn:
        screen('God created\neverything')
        moodometer=[1,2,3,4,4,4,4,4]
    elif 'was' in qstn and 'talking' in qstn:
        screen('oh sorry')
        moodometer=[1,2,3,4]
    elif 'pause' in qstn or 'elevator' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/wait.mp3')
        moodometer=[1,2,3,4,5]
    elif 'monkey' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/Monkeys-Spinning-Monkeys.mp3')
        moodometer=[1,2,3,4,5]
    elif 'because' in qstn and 'answer' in qstn or 'terrible' in qstn and 'answer' in qstn:
        screen('yes it is')
        moodometer=[1,2,3,4,5,5]
    elif 'birthday' in qstn or 'Birthday' in qstn:
        os.system('vlc /usr/share/code/project/Happy_birthday/1.mp3')
        moodometer=[1,2,3,4]
    elif 'look good' in qstn or 'look nice' in qstn:
        screen('thanks!')
        moodometer=[2,4,4,4,4]
    elif 'jazz' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/jazz.mp3')
        moodometer=[1,2,3,4,5] 
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
    elif 'cake' in qstn or 'cookie' in qstn or 'ice cream' in qstn or 'sugar' in qstn or 'pie' in qstn:
        screen('absolutely not\nits bad for you')
        moodometer=[1,2,3,4,4]
    elif 'cheeseburger' in qstn:
        screen('yes indeed')
        moodometer=[1,2,3,4,4,4,5]
    elif 'fluffing a duck' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/Fluffing-a-Duck.mp3')
        moodometer=[1,2,3,4,5]
    elif 'digital world' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/digital-world.mp3')
        moodometer=[1,2,3,4,5]
    elif 'oh' in qstn:
        screen('yep')
        moodometer=[1,2,3,4,5]
    elif 'elf' in qstn:
        screen('the tiny one\nis near')
        moodometer=[1,2,3,4,4,4,5]
    elif 'guard' in qstn:
        guard()
        screen('got you')
        moodometer=[1,2,3,4,5]
    elif 'Detroit' in qstn:
        screen('best teams')
        moodometer=[1,2,2,2,2,2,2,2]
    elif 'car' in qstn:
        screen('cheese')
        moodometer=[1,2,3,4,4,4,5]
    elif 'my name' in qstn:
        screen(your_name)
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
    elif 'logo' in qstn:
        os.system('gpicview '+username+'/Pictures/Mrpi314.gif')
        moodometer=[1,2,3,4,5]
    elif 'fire' in qstn:
        print('1. unplug me\n2. pack me up\n3. carefully take me out of the house\n4. go back in and save my keyboard')
        screen('look in shell\nfor result')
        moodometer=[1,2,3,5]
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
    elif 'exit' in qstn or 'leave' in qstn:
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
    elif 'sad' in qstn or 'bad' in qstn or 'angry' in qstn or 'depressed' in qstn or 'mean' in qstn:
        screen('I hope you\nfeel better soon')
        moodometer=[1,2,3,4,4,4,4,4,4,5]
    elif 'attack' in qstn or 'Attack' in qstn:
        kilw=input('who are you attacking?')
        mis=range(50,70)
        far=range(30,47)
        dl=range(20,60)
        damage=0
        atk=range(10,90)
        slfd=100
        while True:
            if 'DH64' in kilw:
                hkil=input('how would you like to attack: missle, fart, or duel')
                if 'missle' in hkil:
                    missle()
                    misd=random.choice(mis)
                    damage+=misd
                    print('damage done:')
                    print(misd)
                elif 'fart' in hkil:
                    stinky()
                    fard=random.choice(far)
                    damage+=fard
                    print('damage done:')
                    print(fard)
                elif 'duel' in hkil:
                    rockpaper()
                    dld=random.choice(dl)
                    damage+=dld
                    print('damage done:')
                    print(dld)
                else:
                    print('miss type! lose turn')
                if damage >= 100:
                    print('you beat DH64!')
                    break
                else:
                    print('damage to go:')
                    print(100-damage)
                time.sleep(2)
                print('\nDH64 attack!')
                time.sleep(1)
                atkk=random.choice(atk)
                slfd=slfd-atkk
                print('you have')
                print(slfd)
                print('health remaining\n')
                time.sleep(2)
                if slfd <= 0:
                    print('you were destroyed by DH64')
                    raise SyntaxError('DH64 has destroyed you')
            else:
                missle()
                break
        moodometer=[1,2,3,4,4,4,4,5]
    elif 'happy' in qstn or 'well' in qstn or 'fine' in qstn or 'good' in qstn or 'wonderful' in qstn:
        screen('that is\nvery good')
        moodometer=[1,2,3,4,4,4,4,4,4,5]
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
    elif 'music' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/music.mp3')
        moodometer=[1,2,3,4,4,4,5]
    elif 'missle' in qstn:
        missle()
        moodometer=[1,2,3,4,5]
    elif 'rock' in qstn and 'paper' in qstn or 'game' in qstn:
        rockpaper()
        moodometer=[1,2,3,4,4,5]
    elif 'thanks' in qstn:
        screen('your welcome')
        moodometer=[1,2,3,4,4,4,4,4,5]
    elif 'you' in qstn and 'food' in qstn:
        screen('My favorite food\nis fresh electrons')
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
        moodometer=[1,2,3,5]
    elif 'welcome' in qstn:
        screen('thanks')
        moodometer=[1,2,3,4,4,4]
    elif 'sleep' in qstn or 'stop talking' in qstn or 'shut up' in qstn:
        sleep()
        moodometer=[1,2,3,4,5]
    elif 'bomb' in qstn:
        os.system('vlc '+username+'/UC37software/sounds/explosions.mp3')
        moodometer=[1,2,3,4,5]
    elif 'calculator' in qstn:
        screen('look in shell\nfor result')
        dg1=int(input('type the first number'))
        print(dg1)
        op=input('type the operator(multiplication=*addition=+subtraction=-division=/)')
        print(op)
        dg2=int(input('type the last number'))
        print(dg2)
        if '*' in op:
            answer=dg1*dg2
        if '+' in op:
            answer=dg1+dg2
        if '-' in op:
            answer=dg1-dg2
        if '/' in op:
            raise SyntaxError('You actually think Im smart enough to do division?')
        print(answer)
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
    elif 'camera' in qstn or 'Camera' in qstn:
        import numpy as np
        import cv2
        faceCascade = cv2.CascadeClassifier('/home/'+username+'/Documents/Face_recognition/Cascades/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        cap.set(3,1280) # set Width
        cap.set(4,960) # set Height
        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5
                ,     
                minSize=(20, 20)
            )
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
            cv2.imshow('IM WATCHING YOU!',img)
            k = cv2.waitKey(30) & 0xff
            if k == 27: # press 'ESC' to quit
                break
        cap.release()
        cv2.destroyAllWindows()
        moodometer=[1,2,3,4,5]
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
    elif 'systems.die' in qstn:
        raise SystemError('code expelled: failed to procced')
    elif 'ok' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5]
    elif 'foot' in qstn:
        screen('you mean the smelly things on the ends of human legs?')
        moodometer=[1,2,3,4,4,4,5]
    elif 'command line' in qstn:
        piatras=input('what would you like to run?: ')
        cmdl(piatras)
        moodometer=[1,2,3,4,4,4,4,5]
    elif 'time' in qstn:
        ntime()
        moodometer=[1,2,3,4,5]
    elif 'party' in qstn:
        party()
        screen('that was fun')
        moodometer=[1,2,3,4,4,4,4]
    elif 'cold' in qstn:
        screen('thats not good')
        moodometer=[1,2,3,4,4,5]
    elif 'cavern' in qstn or 'Cavern' in qstn:
        cavern()
        moodometer=[1,2,3,4,5]
    elif 'Lions' in qstn and 'stink' in qstn or 'suck' in qstn or 'bad' in qstn:
        screen('Thay may be bad, but if I switched teams, that would make me a bandwagon')
        moodometer=[1,2,3,4]
    elif 'my favorite color' in qstn or 'red' in qstn or 'green' in qstn or 'blue' in qstn or 'yellow' in qstn or 'orange' in qstn or 'purple' in qstn or 'pink' in qstn:
        screen('Oh, My favorite is Amaranth')
        moodometer=[1,2,3,4]
    elif 'favorite color' in qstn:
        screen('Amaranth')
        moodometer=[1,2,3,4,5]
    elif 'movie' in qstn or 'I watch' in qstn:
        print('anything with Wall-e or the Jetsons')
        screen('look in shell\nfor result')
        moodometer=[1,2,3,4,5]
    elif 'sports' in qstn:
        screen('look in shell\nfor result')
        team = input('what team')
        url=team+'+score&oq=lions+score&aqs=chrome..69i57.4272j0j7&sourceid=chrome&ie=UTF-8'
        print('https://www.google.com/search?q='+url)
        moodometer=[1,2,3,4,5]
    elif 'LED' in qstn:
        if 'off' in qstn:
            LEDoff()
        elif 'on' in qstn:
            LEDon()
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
    elif 'connect' in qstn:
        print('connecting to Y-PHI')
        cwifi()
        moodometer=[1,2,3,4,4,4,5]
    elif 'want' in qstn:
        screen('you want it,\nbut do you need it?')
        moodometer=[1,2,3,4,5,5]
    elif 'no' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5,5,5]
    elif 'Bible' in qstn or 'verse' in qstn:
        bible()
        moodometer=[1,2,3,4,5]
    elif 'build' in qstn:
        screen('look in shell\nfor result')
        task=input('do I have arms?')
        if 'no' in task or 'No' in task:
            print('then why would I be able to build something?')
        else:
            print('the correct answer is no.\ntherefore, I can not build something.')
        moodometer=[1,2,3,4,5,5,5,5]
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
        moodometer=[2]
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
    print('\n\n')
psaid=[]
wign=[]
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
        screen("no, "+qstn)
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
    print('\n\n')
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
def kasaon():
    asyncio.run(ks.SmartPlug(kasaip).turn_on())
def kasaoff():
    asyncio.run(ks.SmartPlug(kasaip).turn_off())
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
def party():
    screen('party!')
    LEDon()
    os.system('vlc '+username+'/UC37software/sounds/music.mp3')
    LEDoff()
def beep():
    screen('A')
rsponce=['']
crsponce=['']
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
def cmdl(text):
    os.system(text)
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
def guard():
    screen('I found no one')
def sleep():
    screen('I am asleep')
    awake=input(' ')
    screen('I am awake')
def good():
    os.system(username+'/UC37software/images/AI-succeed-gif')
def clear_shell():
    for i in range(0,25):
        print('\n')
clear_shell()
print('====================UC37====================')
st=0
greet='hello, %s' % your_name
speak(greet)
fill=0
lasts=' '
print('Process completed')
notned=0
while True:
    if voice == True:
        while True:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                if st == 0:
                    clear_shell()
                    st=1
                    print('====================UC37====================')
                    past=['z','z','z','z']
                print('...')
                audio=r.listen(source)
                try:
                    saidtxt=r.recognize_google(audio)
                    notned=0
                except:
                    notned+=1
                    break
            if saidtxt == 'what' or 'pardon' in saidtxt:
                speak("I")
                if mood == 5:
                    mquestion(saidtxt)
                else:
                    question(saidtxt)
            else:
                speak("I")
                if mood == 5:
                    mquestion(saidtxt)
                else:
                    question(saidtxt)
                lasts=saidtxt
                data.insert(0, int(mood))
                if len(data) >= 5:
                    data.pop(3)
                #print(data)
                jsaid.insert(0, saidtxt)
                #print(jsaid)
                #print(rsponce)
                #print(crsponce)
                #print(psaid)
                ml=most_frequent(data)
        if notned==1:
            speak('I')
            screen('La dee dum')
        elif notned==2:
            speak('I')
            screen('Im bored')
        elif notned==3:
            speak('I')
            os.system('vlc '+username+'/UC37software/sounds/Monkeys-Spinning-Monkeys.mp3')
            notned=0
    else:
        saidtxt=input('..:')
        question(saidtxt)