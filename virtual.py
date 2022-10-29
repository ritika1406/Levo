from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from socket import timeout
from plyer import notification        #package for notification
import time   
import random
from enum import IntEnum

listener = sr.Recognizer()              #voice recognization
engine = pyttsx3.init()                 #speech package
voices = engine.getProperty('voices')        #different voice of alexa
engine.setProperty('voice', voices[1].id)      #setting to female version of voices



def talk(text):
    engine.say(text)                      
    engine.runAndWait()

def talk_command():
        try:
            with sr.Microphone() as source:                   #setting microphone as a source
               print("listening")        
               voice = listener.listen(source)               #what was the context from the source
               command = listener.recognize_google(voice)            #recognixe the voice and conversion with the help of google api
               command = command.lower()                               #convert it to lower case
               if 'alexa' in command:
                    command=command.replace('alexa', '')                                    #if alexa in the sentence then only print the value    
                    talk(command)
        except:
            pass
        return command

class Action(IntEnum):            #stone paper scissor notation
    Rock = 0
    Paper = 1
    Scissor = 2 


def run_alexa():                                                   #performing function
    command= talk_command()
    print(command)
    if 'play' in command:                                         #plays youtube videos
        song = command.replace('play', '')
        talk('playing')
        print('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:                                        #informs about the current time
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'wikipedia' in command:                                    #reads wikipedia
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'alarm' in command:                                        #sets alarm
        print("In how many minutes?")
        local_time = float(input())
        local_time= local_time * 60
        notification.notify(title="break reminder", message="Take a break", timeout=1)
        
    elif 'rock'or'paper' or 'scissor' in command:                      #plays stone paper scissor
        user_input = input("Enter any number Rock=0, Scissor=2, Paper=1\n")
        userinput= int(user_input)
        user_input= Action(userinput)
        comp_inputt= random.randint(0, len(Action)-1)
        comp_input= Action(comp_inputt)

        if user_input == comp_input:
            print("Draw")
        elif user_input == Action.Rock:
            if comp_input==Action.Scissor:
                print("Win")
            else:
                print("Lose")
        elif user_input == Action.Paper:
            if comp_input == Action.Scissor:
                print("Lose")
            else:
                print("Win")
        elif user_input == Action.Scissor:
            if comp_input == Action.Paper:
                print("Win")
            else: 
                print("lose")
        else:
            print("no such")

run_alexa()