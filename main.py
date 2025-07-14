import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


r = sr.Recognizer()
engine = pyttsx3.init() #Initialize engine

newsapikey = os.getenv("new_api_key")
openaiapikey = os.getenv("openAi_api_key")


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key = openaiapikey
    )

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"
            },
            {
                "role": "user",
                "content": command
            }

        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith("play"):
        # song = c.lower().split(" ")[1]
        song = c.lower().replace("play", "").strip()
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=India&sortBy=publishedAt&apiKey={newsapikey}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Speak the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAi handle the requests
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        
        # Listen for the wake word: "Jarvis"
        # Obtain audio from the microphone

        print("Recognising...")

        try:
            #Use microphone as source
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2) #Will raise error if no speech in 5 seconds
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Yes, How can I help you?")
                # Listen for Command 
                with sr.Microphone() as source:
                    print("Jarvis is listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

          
        except Exception as e:
            print("Error; {0}".format(e))