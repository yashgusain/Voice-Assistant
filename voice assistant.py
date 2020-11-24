import speech_recognition as sr
import texttospeech as ttos
import wiki
import dateandtime
import pyjokes
import screenshot as ssc

def sayprime():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        greet = dateandtime.datentime('wish') + "how may i help you"
        ttos.speak(greet)
        print("im listening")
        try:
            audio = r.listen(source)  # record voice
        except sr.WaitTimeoutError:
            print("mic is not getting any voice")
        query = r.recognize_google(audio)
        print(r.recognize_google(audio))
        return query


def saysecondary():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        ttos.speak("any other instructionn you want me to do")
        print("im listening")
        try:
            audio = r.listen(source)  # record voice
        except sr.WaitTimeoutError:
            print("mic is not getting any voice")
        query = r.recognize_google(audio)
        print(r.recognize_google(audio))
        return query


# features
def repeat():
    query = sayprime()
    if 'date' in query or 'time' in query:  # date and time
        resultdati = dateandtime.datentime(query)
        # print(resultdati)
        ttos.speak(resultdati)

    elif 'who' in query or 'what' in query:  # wikipedia search
        ttos.speak(wiki.wi(query))

    elif "tell me a joke" in query or 'joke' in query:  # telling joke
        joke = pyjokes.get_joke(language='en', category='all')
        ttos.speak(joke)

    elif "take screenshot" in query or 'capture' in query:  # take screenshot
        ssc.sshot()
        ttos.speak("screenshot sucessfully taken")
    elif "how are you" in query or "how you doing" in query:
        ttos.speak("im good,how are you ")
    else:
        print("this feature coming soon")
    print("you want me to continue")
    permission = saysecondary()
    if permission == "yes":
        repeat()
    else:
        return "thanks"


repeat()
