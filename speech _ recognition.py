import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech from the microphone
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        speak("Say something...")
        
        # Adjust for ambient noise and listen to the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Use Google Web Speech API to recognize the speech
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            speak(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
            speak("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            speak("Could not request results from Google Speech Recognition service.")

# Call the function to start voice recognition
recognize_speech()
