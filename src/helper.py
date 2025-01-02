import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import re

print("perfect!!")
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY



def voice_input():
    r=sr.Recognizer()
    
    # Check if a microphone is available
    try:
        if not sr.Microphone.list_microphone_names():
            raise OSError("No input device available. Please use text input.")

        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text

    except OSError:
        # Fallback to text input if no microphone is available
        print("Microphone not available. Please type your input.")
        text = input("Input: ")
        return text
    

def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")

def llm_model_object(user_text):
    #model = "models/gemini-pro"
    
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text

    # Remove '**' formatting
    clean_result = re.sub(r'\*{1,2}', '', result)
    
    return clean_result
