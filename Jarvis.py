import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate','150')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    speak(" How can I help you ? ")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please")
        return "None"
    return query



'''def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('projectjarvis01@gmail.com','jgmzqubrjjruzyyr')
    server.sendmail('projectjarvis01@gmail.com',to ,content)
    server.close()'''
    
def startExec():
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)   
   

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com/")
            speak("opening youtube")

        elif 'show me youtube' in query:
            speak("Sir what would you like to watch")
            en = takeCommand()
            webbrowser.open(f"https://www.youtube.com/results?search_query={en}")


        elif 'open google' in query:
            Chromepath = ("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            speak("ok sir")
            webbrowser.open(Chromepath)

        elif 'search' in query:
            speak("Sir what should i search")
            gk = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={gk}")

            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is: {strTime}")
            print(strTime)                


        elif 'shutdown' in query:
            speak('do you want to shutdown the system Sir')
            reply = takeCommand()
            if "yes" in reply:
                os.system('shutdown /s /t 1')
            else:
                break    

        elif 'restart' in query:
            speak('do you want to restart the system Sir')
            reply = takeCommand()
            if "yes" in reply:
                os.system('shutdown /r /t 1')
            else:
                break 


        elif 'open classroom' in query:
            webbrowser.open_new_tab('https://classroom.google.com/u/1/h') 
            speak('opening classroom')


        elif 'open notepad' in query:
            path = 'C:\\Windows\\system32\\notepad.exe'
            speak('There you go')
            os.startfile(path)

        elif 'close notepad' in query:
            os.system('TASKKILL /F /IM notepad.exe')
            speak('ok sir')


        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm:
                srTime = datetime.datetime.now().strftime(" %I:%M %p")
                file.write(srTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read())


        elif "locate" in query:
            query = query.replace("locate", "")
            location = query
            speak("ok sir, locating")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")



        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

        elif 'your features' in query:
            speak('''I can perform various tasks that include telling current time, opening google, youtube and
            some other sites ''')
            speak("I can write a note for you, locate a particular location, search things on google, youtube and wikipedia")
            speak("I can also shutdown and restart your computer")
            speak("what can i do for you sir")










        elif 'hello jarvis' in query:
            speak('hello sir, i hope your fine')  

        elif 'who are you' in query:
            speak('I am Jarvis and I am an voice assistant to help you')

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir") 

        elif 'fine' in query:
            speak("It's good to know that your fine")

        elif 'alright' in query:
            speak('What else can I do for you Sir ')  

        elif 'reason for your creation' in query:
            speak("I was created as a Minor project")   

        elif 'thank you' in query:
            speak("it was my pleasure Sir any thing else ")

        elif 'exit' in query:
            speak("it was nice talking to you Sir ")
            exit()

        else:
            speak("sorry sir i did not get that")

if __name__ == "__main__":
    wishMe()
    startExec()        