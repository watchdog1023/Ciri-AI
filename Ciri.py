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
#For MP3 Playback
from pygame import mixer
#Voice Recg
import speech_recognition as sr 
#For Threading
#from threading import Thread
from time import sleep

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
    mixer.init()
    mixer.music.load("voice/" + mp3 + ".mp3")
    mixer.music.play()

def learn():
    print('Learn')
    exit()
        
def greetings():
    TTS("Hi,I'm Ciri")
    print("Hi,I'm Ciri")
    localtime = time.asctime(time.localtime(time.time()))
    print("Current Local Time:" + localtime)
    TTS("current local time is " + localtime)
    TTS("What is your Name?")
    name = input("What is your Name?\n")
    print("Your name is " + name)
    if name == "bob":
        print("You are not welcome here")
        exit()
    else:
        print("Nice to meet you " + name)
        TTS("nice to meet you " + name)
    TTS("what do you want me to do?")
    do = input("What do you want me to do?")
    if do == "learn":
        ltsm()
    elif do == "learn".upper():
        ltsm()
    elif do == "learn".lower():
        ltsm()
    elif do == "Learn":
        ltsm()
    elif do == "add memo":
        memo()
    elif do == "die":
        die()
    elif do == "die".lower():
        die()
    elif do == "Die":
        die()
    elif do == "die".upper():
        die()
    elif do == "help":
        print("Here is a list of commands I recgoize")
        print("Die\n")
        print("Learn\n")
        print("Add memo\n")
        print("Help\n")
    else:
        print("OK")
  
greetings()
