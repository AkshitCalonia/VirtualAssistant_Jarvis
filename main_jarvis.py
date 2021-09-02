import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import smtplib
import os

# Remember to install all these via pip, before running the program !!

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak("I am Jarvis Sir. Please let me know how can I help you?")

def takecommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.energy_threshold = 440 #set as per the background noises around you 
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('myemail@gmail.com', 'my-password-here') #put your personal pass and id here, through which email has to be sent
    # Remember to go on to you google gmail account settings and enable - allow less secure apps, then only the email is going to be sent!
    server.sendmail('myemail@gmail.com', to,  content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        
        # NOW COMES LOGIC
        if 'wikipedia' in query:
            speak('searching wikipedia, Stand by,')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            try:
                speak("According to wikipedia,")
                speak(results)
            except Exception as e:
                print(e) # Print the error if you want
                speak(f"Sorry, no page exists for {query}, in wikipedia!")
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open tonication' in query:
            webbrowser.open('tonication.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\parve\\OneDrive\\Desktop\\Dekstop Material\\my_songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the current time is {strtime}")
        
        elif "open code" in query:
            os.startfile("C:\\Users\\parve\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'email to me' in query:
            try:
                speak("what should I say to him?")
                content = takecommand()
                speak("Sending the mail, Stand by!")
                to = "The_gmail_on_which_email_should_be_sent@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, can't able to send email at the movement, try later!")

        elif 'quit' in query:
            speak("Thank you for using me! See you later")
            break

        else:
            speak("Sorry, I Didn't quite get that, please repeat!")