import pyttsx3
import speech_recognition as sr
from Web import Browser 
import os
import random
import datetime


engine = pyttsx3.init()
      

def launch():
    engine.setProperty('rate',300)
    speak("Activating Elssa PC voice Assistant")
    engine.setProperty('rate',180)    
    speak("Hello, My name is Elsa. I am your voice assistant. how can i help you ?")
    

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.8
        r.energy_threshold = 10000
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"user said : {text}\n")
        
    except Exception as e:
        print("Say that again Please...")
        return "None"
    return text
    
if __name__=="__main__":
    launch()    
    def open():
        while True:
            text = take_command().lower()
            
            if 'elsa' in text:
                speak("Yes Sir,tell me, what can i do for you")
                open()
                
            elif "information" in text or "details" in text:
                speak("you need information related to which topic?")
                infor = take_command()
                speak("searching {} in wikipedia".format(infor))    
                browser =Browser()
                browser.open_url_wikipedia(infor)
                
            elif 'open' in text and 'google' in text:
                speak("what can i search on Google ?")
                search = take_command()
                speak("searching {} in Google".format(search))
                browser =Browser()
                browser.open_url_google(search)
                
            elif 'open' in text and 'youtube' in text:
                speak("which video you want watch ?")
                search = take_command()
                speak("Opening the {} on YouTube".format(search))
                browser =Browser()
                browser.open_url_youtube(search)
                
            elif 'close' in text and 'chrome' in text:
                os.system("taskkill /f /im chrome.exe")
                speak("Closing Chrome")
                
            elif 'play' in text and  'music' in text:
                music_dir = "E:\Music"
                songs = os.listdir(music_dir)
                speak("Opening Music Player")
                os.startfile(os.path.join(music_dir,random.choice(songs)))
                
            elif 'open vs code' in text:
                os.startfile('C:\Microsoft VS Code\Code.exe')
            elif 'close' in text and  'vs' in text and  'code' in text:
                os.system("taskkill /f /im Code.exe")
                
            elif 'what' in text and 'time' in text:
                time = datetime.datetime.now().strftime('%H:%M:%S')
                speak(time)
            
            elif 'shut' in text and  'down' in text:
                os.system("shutdown /s /t 1")
            elif 'restart' in text:
                os.system("restart /r /t 1")                      
open()    