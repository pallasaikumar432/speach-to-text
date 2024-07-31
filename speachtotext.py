import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as the source of input
with sr.Microphone() as source:
    print("Please say something")
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Google Web Speech could not understand the audio")
    except sr.RequestError:
        print("Could not request results from Google Web Speech service")
