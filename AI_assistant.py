import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
#import pyjokes

from wikipedia.wikipedia import search

engine= pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[2].id)
newvoicerate =300
engine.setProperty('rate', newvoicerate)

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("prachiipandey2002@gmail.com","prachi@12345")
    server.sendmail("prachiipandey2002@gmail.com",to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\Supriya\\Desktop\\song\\ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+ usage)
    battery=psutil.sensors_battery
    speak("battery is at",battery.percent)
    speak(battery)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time =datetime.datetime.now().strftime('%H:%M:%S')   
    speak(time)

def date():
  year=int(datetime.datetime.now().year)
  month=int(datetime.datetime.now().month)
  date=int(datetime.datetime.now().day)
  speak("The current date is ")
  speak(date)
  speak(month)
  speak(year)
  
def wishme():
    speak("Welcome back Mam!")
    time()
    date()
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")    
    elif hour>=18 and hour<=24:
        speak("Good Evening")    
    else:
        speak("Good Night")    
        
    speak("Friday at your service. How can I help you?")
#def jokes():
   # speak(pyjokes.get_jokes())    
    
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
        
    try:
        print("Recognizing")  
        query=r.recognize_google(audio,language='en=US') 
        print(query)    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query= takeCommand().lower()
        print(query)
        
        if "time" in query:
            time()
        elif "date" in query:
            date()  
        elif "offline" in query:
            quit()      
        elif "wikipedia" in query:
            speak('Searching')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            speak(result)
        elif "send email" in query:  
            try:
                speak("what should i say?")
                content=takeCommand()
                speak("Please type email of the recevier")
                to=input()
                sendmail(to,content) 
                speak(content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")    
                
        elif  "search in chrome" in query:
            speak("what should i search?")
            chromepath= "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            try:
                #wb.register('chrome',None)
                search=takeCommand().lower()
                mybrowser=wb.get(chromepath)
                mybrowser.open_new_tab(search)
            except Exception as  e: 
                print(e)
                     
        elif "logout" in query:
            os.system("shutdown - l")    
            
        elif "shutdown" in query:
            os.system("shutdown /s /t l")     
        elif "restart" in query:
            os.system("shutdown /r /t l")         
        elif "play songs" in query:
            song_dir="C:\\Users\\Supriya\\Desktop\\song"
            songs=os.listdir(song_dir)  
            os.startfile(os.path.join(song_dir,songs[0]))        
        elif "remember that" in query:
            speak("what i remember?")
            data=takeCommand()
            speak("you said me to remember"+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that"+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done!")    
        elif "cpu" in query:
            cpu()    
        #elif  "jokes" in query:
            # jokes()
                   
               