from __future__ import absolute_import, division, print_function
from six import moves
import sys
import getopt
import os
import random
import ssl
import string
import base64
import time
#TTS
import pyttsx3
#For Deep Learning
import numpy as np
#import tflearn
#from tflearn.data_utils import *
#import tensorflow as tf
#Voice Recg
import speech_recognition as sr 
#For Threading
#from threading import Thread
from time import sleep
import Family_Tree

state = None

def STT():
    r = sr.Recognizer()
    sr.Microphone.list_microphone_names()
    micin = input("Please Select your mic[number in only,first device is number 0]")
    mic = sr.Microphone(device_index = micin)
    with mic as source:
        playMP3("talk")
        audio = r.listen(source)
    output = r.recognize_sphinx(audio)
    #if output == "":
    #    
    #elif output == "":
    #    elif output == "":
    #    
    #else:
    #    playMP3("understand")
    #    print("I can not understand you")

def TTS(phase):
    engine = pyttsx3.init()
    engine.say(phase)
    engine.runAndWait()

def die():
    print("No")
    why = input("Why do you want me to die?\n")
    if why == "":
        print("it")

def memo_check():
    pass

def memo():
    pass

def playMP3(mp3):
    #For MP3 Playback
    from pygame import mixer
    mixer.init()
    mixer.music.load("voice/" + mp3 + ".mp3")
    mixer.music.play()

def learn():
    print('Learn')
    exit()
        
def greetings():
    global state
    global name
    if os.path.exists("name.txt") is True:
        fi = open("name.txt","r+")
        contents = fi.read()
        state = False
        name = contents
    else:
        file1 = open("name.txt","w+")
        file1.close()
        fi = open("name.txt","r+")
    if state is True:
        TTS("Hi,I am Cirilla,but you can call me ciri")
        print("Hi,I'm Ciri")
    localtime = time.asctime(time.localtime(time.time()))
    print("Current Local Time:" + localtime)
    if state is True:
        TTS("current local time is " + localtime)
    if state is True:
        TTS("What is your Name?")
        names = input("What is your Name?\n")
        name = names
        fi.write(name)
        fi.close()
        
    if state is False:
        print("Welcome Back " + name)
        TTS("Welcome Back " + name)

    if name == "bob":
        print("You are not welcome here")
        exit()
    else:
        if state is True:
            print("Nice to meet you " + name)
            TTS("nice to meet you " + name)

    TTS("what do you want me to do?")
    do = input("What do you want me to do?\n")
    if do == "add memo":
        memo()
        state = False
    elif do == "die":
        die()
        state = False
    elif do == "die".lower():
        die()
        state = False
    elif do == "Die":
        die()
        state = False
    elif do == "die".upper():
        die()
        state = False
    elif do == "quit":
        return 0
    elif do == "help":
        TTS("Here is a list of commands I recognise")
        print("Here is a list of commands I recognise")
        print("Die")
        print("Learn")
        print("Add memo")
        print("Help")
        sleep(5)
        state = False
        greetings()
    else:
        print("OK")

if __name__ == '__main__':  
    state = True
    greetings()
