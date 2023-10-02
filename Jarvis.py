import os
import sys
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser
import smtplib
import random

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Get your own key')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 3].id)


def talk(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
        talk('Boss!, Good Morning!')

    elif CurrentHour >= 12 and CurrentHour < 18:
        talk('Boss! Good Afternoon!')

    elif CurrentHour >= 18 and CurrentHour != 0:
        talk('Boss! Good Evening!')


greetMe()

talk('I\'m  your assistant Jarvis!')
talk('tell me about today?')


def GivenCommand():
    k = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        k.pause_threshold = 1
        audio = k.listen(source)
    try:
        Input = k.recognize_google(audio, language='en-in')
        print('Boss: ' + Input + '\n')

    except sr.UnknownValueError:
        talk('Sorry Boss! I didn\'t get that! Try typing it here!')
        Input = str(input('Command: '))

    return Input


if __name__ == '__main__':

    while True:

        Input = GivenCommand()
        Input = Input.lower()

        if 'open google' in Input:
            talk('sure')
            webbrowser.open('www.google.com')

        elif 'open gmail' in Input:
            talk('sure')
            webbrowser.open('www.gmail.com')
            
        elif 'open youtube' in Input:
            talk('sure')
            webbrowser.open('www.youtube.com')

        elif "what\'s up?" in Input or 'how are you?' in Input:
            setReplies = ['Just doing some stuff!', 'I am good!', 'Nice!', 'I am amazing and full of power']
            talk(random.choice(setReplies))
       
        elif "who are you?" in Input or 'where are you?' in Input or 'what are you?' in Input:
            setReplies = [' I am Jarivs!', 'In your system', 'I am an example of AI']
            talk(random.choice(setReplies))

        elif 'email' in Input:
            talk('Who is the recipient? ')
            recipient = GivenCommand()

            if 'me' in recipient:
                try:
                    talk('What should I say? ')
                    content = GivenCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    talk('Email sent!')

                except:
                    talk('Sorry ! I am unable to send your message at this moment!')

        elif 'nothing' in Input or 'abort' in Input or 'stop' in Input:
            talk('okay')
            talk('Bye, have a good day.')
            sys.exit()

        elif 'hello' in Input:
            talk('hey')

        elif 'Jarivs!' in Input:
            talk('Yes! Boss.')

        elif 'bye' in Input:
            talk('Bye, have a great day.')
            sys.exit()


        elif 'play music' in Input:
            music_dir = 'Your_Music_Path'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'show images' in Input:
            image_dir = 'Your_Image_Path'
            image = os.listdir(image_dir)
            print(image)    
            os.startfile(os.path.join(image_dir, image[0]))

            talk('Okay, here are your images! Have Fun!')

        elif 'the time' in Input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            talk(f"Boss, the time is {strTime}")

        elif 'open vs code' in Input:
            codePath = "Your_VSCode_Path"
            os.startfile(codePath)

        else:
            Input = Input
            talk('Searching...')
            try:
                try:
                    res = client.Input(Input)
                    outputs = next(res.outputs).text
                    talk('Alpha says')
                    talk('Gotcha')
                    talk(outputs)

                except:
                    outputs = wikipedia.summary(Input, sentences=3)
                    talk('Gotcha')
                    talk('Wikipedia says')
                    talk(outputs)


            except:
                    talk("searching on google for " + Input)
                    say = Input.replace(' ', '+')
                    webbrowser.open('https://www.google.co.in/search?q=' + Input)



        talk('Next Command! Please!')

#to be continued...
