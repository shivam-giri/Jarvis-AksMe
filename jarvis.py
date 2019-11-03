import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,  Shivam")

    elif hour>=12 and hour<18:
        speak("Good Eveing, Shivam")

    else:
        speak("Good Night Shivam ")

    speak("Hey Shivam, I am jarvis. please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        speak("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mahant1598shivam@gmail.com','mahantshivam')
    server.sendmail('mahant1598shivam@gmail.com', to ,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing tasks based on querry:
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            resuls = wikipedia.summary(query, sentences=2)
            speak("Acoording to wikipedia")
            print(resuls)
            speak(resuls)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open tutorialspoint' in query:
            webbrowser.open('tutorialspoint.com')

        elif 'play music' in query:
            music_dir = 'E:\\luvy\\new music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M::%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Mahant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to nirmal' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "nirmalpatidar048@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                speak("sorry bhai, i am not able to send this maail")

        elif 'quit' in query:
            exit()