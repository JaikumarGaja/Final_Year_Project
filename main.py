import os
import datetime
import tkinter
from tkinter import scrolledtext
from youtube_search import YoutubeSearch
import PIL
from PIL import Image, ImageTk
import speech_recognition as sr
# import pyaudio
import wikipedia
import pyjokes
import webbrowser
# import pytime

from googlesearch import search
import pyttsx3
import requests
import AppOpener
# from threading import *
# import urllib.request, bs4 as bs, sys, threading
import threading
from tkinter import *
from functools import partial
import winsound
import re


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class SpeakRecog:
    def __init__(self,scrollable_text):
        self.scrollable_text=scrollable_text

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def updating_ST(self, data):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end', data + '\n')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()

    def speak(self, audio):
        """It speaks the audio"""
        self.updating_ST(audio)
        self.engine.say(audio)
        # engine.save_to_file('Hello World', 'test.mp3')
        self.engine.runAndWait()

    def print(self, data):
        self.updating_ST(data)

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        SR.print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        SR.print("Recognizing...")
        queryString = r.recognize_google(audio, language='en-in')
        SR.print(f"User said: {queryString}\n")
    except Exception as e:
        # print(e)
        SR.print("Unable to Recognize your voice.")
        return "None"
    return queryString


# def speak(audio):
#     engine.say(audio)
    # engine.runAndWait()


def weather(queryString):
    if queryString.startswith('weather of'):
        li = list(queryString.split(" "))
        loc_base = "http://api.openweathermap.org/geo/1.0/direct?q="
        apikey = "9bf14a035688f500531aa388ffefac84"
        city = li[2]
        loc_url = loc_base + city + "&appid=" + apikey
        response = requests.get(loc_url).json()
        lat = response[0]["lat"]
        lon = response[0]["lon"]
        base = "https://api.openweathermap.org/data/2.5/weather?lat="
        url1 = base + str(lat) + "&lon=" + str(lon) + "&appid=" + apikey + "&units=metric"
        response1 = requests.get(url1).json()
        temp = response1['main']['temp']
        feels_like = response1['main']['feels_like']
        humidity = response1['main']['humidity']
        description = response1['weather'][0]['description']
        # SR.print("Temperature : ", temp)
        # SR.print("Feels Like : ", feels_like)
        # SR.print("Humidity : ", humidity)
        # SR.print("Description : ", description)
        SR.speak(f'The Temperature is {temp}')
        SR.speak(f'It Feels Like {feels_like}')
        SR.speak(f'The Humidity is {humidity}')
        SR.speak(f'It is {description} outside')
    else:
        SR.speak(f'Please Say., Weather. of. city name ')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        SR.speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        SR.speak("Good Afternoon Sir !")

    else:
        SR.speak("Good Evening Sir !")


"""class SpeakRecog:
    def __init__(self,scrollable_text):
        self.scrollable_text=scrollable_text

    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    scrollable_text=None

    def STS(self,scrollable_text):
        # This is scrollable text setter 
        self.scrollable_text=scrollable_text
    def updating_ST(self,data):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end',data+'\n')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()
    def updating_ST_No_newline(self,data):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.insert('end',data)
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.see('end')
        self.scrollable_text.update()
    def scrollable_text_clearing(self):
        self.scrollable_text.configure(state='normal')
        self.scrollable_text.delete(1.0,'end')
        self.scrollable_text.configure(state='disabled')
        self.scrollable_text.update()
    def speak(self,audio):
        # It speaks the audio
        self.updating_ST(audio)
        self.engine.say(audio)
        # engine.save_to_file('Hello World', 'test.mp3')
        self.engine.runAndWait()
        # engine.stop()

    def nonPrintSpeak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def takeCommand(self):
        # It take microphone input from the user and return string
        recog=sr.Recognizer()
        # mic=Microphone()
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source)
            self.updating_ST(SpeakRecog,data="\nListening...")
            recog.pause_threshold = 1
            # r.energy_threshold = 45.131829621150224
            # print(sr.Microphone.list_microphone_names())
            #print(r.energy_threshold)
            audio=recog.listen(source)
        try:
            self.updating_ST(SpeakRecog,data="Recognizing...")
            queryString= recog.recognize_google(audio)
            self.updating_ST(f"You: {queryString}\n")
        except Exception as e:
            # print(e)
            self.updating_ST("Say that again please...")
            return 'None'
        return queryString"""


# def wikipediaFn(queryString):
#     SR.speak('Searching Wikipedia...')
#     queryString = queryString.replace("wikipedia", "")
#     queryString = queryString.replace("Search", "")
#     qs = queryString.replace("in", "")
#     SR.print(qs)
#     results = wikipedia.summary(qs, sentences=3)
#     SR.speak("According to Wikipedia")
#     SR.print(results)
#     SR.speak(results)


def youtube(queryString):
    SR.speak("Here you go to Youtube\n")
    webbrowser.open("youtube.com")


def google(queryString):
    SR.speak("Here you go to Google\n")
    webbrowser.open("google.com")


def stackoverflow(queryString):
    SR.speak("Here you go to Stack Over flow.Happy coding")
    webbrowser.open("stackoverflow.com")


def appOpen(queryString):
    if 'open' in queryString:
        appname = queryString.replace("open","")
    # appname = list(queryString.split(" "))
    # AppOpener.run(appname[1])
        AppOpener.open(appname, match_closest=TRUE)
    # SR.print(appname[1])
        SR.speak("..Ok, sir")
    elif 'close' in queryString:
        appname = queryString.replace("close","")
        AppOpener.close(appname, match_closest=TRUE)
        SR.speak("...OK, Sir, Closing")
def CommandsList():
    os.startfile('Commands.txt')

def search(queryString):

    if 'search' in queryString:
        queryString = queryString.replace("search", "")
        url = "https://www.google.com/search?q="+queryString
        webbrowser.open(url)
    else:
        qs = queryString.replace("play", "")
        # url = "https://www.google.com/search?q="+qs
        # response = requests.get(url)
        # html_content = response.text
        # print(html_content)
        # youtube_links = []
        # urls = re.findall(r'(https?://\S+)', html_content)
        # # urls = re.findall(r'(https?://\S+)', html_content)
        # for url in urls:
        #     if "youtube.com" in url:
        #         youtube_links.append(url)
        # webbrowser.open(youtube_links[1])
        results = YoutubeSearch(qs, max_results=5).to_dict()

        # Get links of videos
        links = []
        for result in results:
            link = 'https://www.youtube.com/watch?v=' + result['id']
            links.append(link)

        webbrowser.open(links[1])


def commands(queryString):
    # if 'wikipedia' in queryString:
    #     wikipediaFn(queryString)

    if 'open youtube' in queryString:
        youtube(queryString)

    elif 'open google' in queryString:
        google(queryString)

    elif 'open stackoverflow' in queryString or 'open stack overflow' in queryString or 'open stack over flow' in queryString:
        stackoverflow(queryString)

    elif 'how are you' in queryString:
        SR.speak("I am fine, Thank you")
        SR.speak("How are you, Sir")
        queryString = takeCommand().lower()
        if 'fine' in queryString or "good" in queryString:
            SR.speak("It's good to know that your fine")


    elif 'joke' in queryString:
        SR.speak(pyjokes.get_joke())

    elif 'exit' in queryString:
        SR.print("User said : Exit")
        SR.print("Thanks for giving me your time")
        SR.speak("Thanks for giving me your time")
        exit()
    elif 'shutdown' in queryString:
        SR.speak("Shutting down PC")
        os.system("shutdown /s /t 1")
    elif 'restart' in queryString:
        SR.speak("Restarting PC")
        os.system("shutdown /r /t 1")
    elif 'weather' in queryString:
        weather(queryString)

    elif 'open' in queryString or 'close' in queryString:
        SR.print(queryString)
        appOpen(queryString)

    elif 'search' in queryString or 'play' in queryString:
        search(queryString)

    elif "write a note" in queryString:
        SR.speak("What should i write, sir")
        note = takeCommand().lower()
        file = open('res/VAW.txt', 'w')
        SR.speak("Noted")
        file.write(note)

    elif "show the note" in queryString:
        SR.speak("Showing Notes")
        file = open("res/VAW.txt", "r")
        # print(file.read())
        SR.speak(file.read())

    elif "none" in queryString:
        SR.speak("Didn't Recognize you")

    elif queryString:
        webbrowser.open(queryString)

    # else:
        # SR.speak("didn't recognize you !")



def mainEntry(event):
    def clearScr():
        var = lambda: os.system('cls')
    # global queryString
    clearScr()
    wishMe()

    while True:
        queryString = takeCommand().lower()
        if 'hello jarvis' in queryString or 'hey jarvis' in queryString or 'jarvis' in queryString:
            winsound.PlaySound('res/Onn.wav', winsound.SND_FILENAME)
            SR.speak('Yes Sir,')
            while True:
                queryString = takeCommand().lower()
                commands(queryString)
                winsound.PlaySound('res/Off.wav', winsound.SND_FILENAME)
                break


def formicbtn():
    event.clear()
    #SR.print("Done")
    winsound.PlaySound('res/Onn.wav', winsound.SND_FILENAME)
    queryString = takeCommand().lower()
    commands(queryString)
    winsound.PlaySound('res/Off.wav', winsound.SND_FILENAME)
    event.set()
    SR.print("Set")

# event2 = threading.Event()
# thread_micbtn = threading.Thread(target=formicbtn, args=(event2,))
# def micbtnThread():
#     event.wait()
#     thread_micbtn.start()
#     event2.wait()
#     event.set()

event = threading.Event()
mainThread = threading.Thread(target=mainEntry, args=(event,))

def micThread():
    Ther= threading.Thread(target=formicbtn)
    Ther.start()

# def gen(n):
#     for i in range(n):
#         yield i


# class MainframeThread(threading.Thread):
#     def __init__(self, threadID, name):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#
#     def run(self):
#         mainEntry()


# def Launching_thread():
#     Thread_ID = gen(1000)
#     global MainframeThread_object
#     MainframeThread_object = MainframeThread(Thread_ID.__next__(), "Mainframe")
#     MainframeThread_object.start()




if __name__ == "__main__":

    window = Tk()
    window.geometry("900x500")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    # enterImgVar = PIL.Image.open('EnterButton.png')
    # enterImg = ImageTk.PhotoImage(enterImgVar)
    enterImg = PhotoImage(file='res/EnterButton.png')
    # micImgVar = PIL.Image.open('MicButton.png')
    # micImg = ImageTk.PhotoImage(micImgVar)
    micImg = PhotoImage(file='res/MicButton.png')
    # Middle Partition
    partition = Canvas(window, bg="#FFFFFF", height=500, width=900, bd=0, highlightthickness=0, relief="ridge")
    partition.place(x=0, y=0)
    partition.create_rectangle(449.0, -1.0, 452.0, 500.0, fill="#000000", outline="")

    # Text Box
    textbox = Entry(window, border=2)
    textbox.place(x=14.0, y=430.0, width=353.0, height=53.0)

    # Text Display
    # myLabel1 = Label(window)
    # myLabel1.place(x=14.0, y=13.0, width=425.0, height=403.0)
    scrollable_text = scrolledtext.ScrolledText(window, state='disabled', relief='sunken', bd=5, wrap=tkinter.WORD, bg='#add8e6', fg='#800000')
    scrollable_text.place(x=14.0, y=13.0, height=410.0, width=425.0)
    SR = SpeakRecog(scrollable_text)
    # SR = takeCommand(scrollable_text)
    # Label Function
    def enterClick(strng):
        keyboardString = strng
        queryString = keyboardString.lower()
        SR.print(keyboardString)
        commands(queryString)

    def onReturn(event):
        value = textbox.get();
        enterClick(value)
        textbox.delete(0, 'end')
    # Enter Button
    myButton1 = Button(window, image=enterImg, borderwidth=0, command=enterClick)
    myButton1.place(x=384.0, y=430.0, width=55.0, height=55.0)
    textbox.bind('<Return>', onReturn)

    # Mic Button
    myButton2 = Button(window, image=micImg, borderwidth=0, bg='white', command=micThread)
    myButton2.place(x=638.0, y=193.0, width=115.0, height=115.0)

    def closing():
        exit()


    myMenu = tkinter.Menu(window)
    m1 = tkinter.Menu(myMenu, tearoff=0)
    m1.add_command(label='Commands List', command=CommandsList)
    myMenu.add_cascade(label="Help", menu=m1)

    window.config(menu=myMenu)
    logo = PhotoImage(file='res/LOGO.png')
    # window.protocol('WM_DELETE_WINDOW', closing)
    window.iconphoto(FALSE, logo)
    mainThread.start()
    window.mainloop()
