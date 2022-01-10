# Import relevant modules:
import pyttsx3
import requests
from Functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from Functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_zoom
from pprint import pprint
from datetime import datetime
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)





# Import relevant modules:
import speech_recognition as sr
from random import choice
from utils import opening_text

# Define function to take user input:
def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-GB')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak(f"Goodnight {USERNAME}, take care!")
            else:
                speak("Have a good day!")
            exit()
    except Exception:
        speak(f"Sorry, I didn't hear anything. Could you please say that again?")
        query = 'None'
    return query

# Define function to prompt engine to speak:
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# Define function to greet user:
def greet_user():

    hour = datetime.now().hour

    if (hour >= 0) and (hour < 12):
        speak(f"Good morning {USERNAME}")
    elif (hour >= 12) and (hour < 17):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 17) and (hour < 24):
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}, How may I assist you?")
    
if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            speak('Opening notepad.')
            open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            speak('Opening command prompt.')
            open_cmd()

        elif 'open camera' in query:
            speak('Opening camera.')
            open_camera()

        elif 'open zoom' in query:
            speak('Opening zoom.')
            open_zoom()

        elif 'open calculator' in query:
            speak('Opening calculator.')
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f"Your IP Address is {ip_address}.\n For your convenience, I'm printing it on the screen sir.")
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia?')
            search_query = take_user_input().lower()
            speak(f"Searching Wikipedia for {search_query}.")
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I'm printing it on the screen.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube?')
            video = take_user_input().lower()
            speak(f"Playing {video} on YouTube.")
            play_on_youtube(video)

        elif 'google' in query:
            speak('What do you want to search on Google?')
            query = take_user_input().lower()
            speak(f"Searching Google for {query}.")
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('To what number should I send the message? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message?")
            message = take_user_input().lower()
            speak(f"Sending message to {number}.")
            send_whatsapp_message(number, message)
            speak("I've sent the message.")

        elif "send an email" in query:
            speak("To what email address should I send the message? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject?")
            subject = take_user_input().capitalize()
            speak("What is the message?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email.")
            else:
                speak("Something went wrong while I was sending the email. Please check the error logs.")

        elif 'joke' in query:
            speak(f"I hope you like this one")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I'm printing it on the screen.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's some advice for you")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I'm printing it on the screen.")
            pprint(advice)

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines")
            speak(get_latest_news())
            speak("For your convenience, I'm printing it on the screen.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        else:
            if query != 'none':
                speak(f"Sorry, I'm not sure what you'd like me to do. What I heard you say was {query}. Could you please repeat your request?")




