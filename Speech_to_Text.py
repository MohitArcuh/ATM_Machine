import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except:
    print("Sorry, could not understand.")

