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
#For Deep Learning
import numpy as np
import tflearn
from tflearn.data_utils import *
import tensorflow as tf
#For MP3 Playback
from pygame import mixer
#Voice Recg
import speech_recognition as sr 
#For Threading
#from threading import Thread
from time import sleep

def STT():
    # get audio from the microphone                                                                       
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
    audio = r.listen(source)   
 
    try:
        print("You said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def die():
    print("No")
    why = input("Why do you want me to die?\n")
    if why == "":
        print("it")

def playMP3(mp3):
    mixer.init()
    mixer.music.load("voice/" + mp3 + ".mp3")
    mixer.music.play()

def learn():
    print('Learn')
        
def greetings():
    playMP3("greetings")
    print("HI,My Name is Ciri")
    name = input("What is your Name?\n")
    print("Your name is " + name)
    if name == "bob":
        print("You are not welcome here")
    else:
        print("Nice to meet you " + name)
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
    else:
        print("OK")
  
greetings()