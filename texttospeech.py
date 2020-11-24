import pyttsx3
def speak(query):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    engine.setProperty('rate',150)
    engine.say(query)
    engine.runAndWait()
