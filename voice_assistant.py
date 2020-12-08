import speech_recognition as sr
import texttospeech as ttos
import wiki
import dateandtime
import pyjokes
import screenshot as ssc
import search_google


def sayprime():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        greet = dateandtime.datentime('wish') + "how may i help you"
        ttos.speak(greet)
        print("im listening")

        audio = r.listen(source)  # record voice

        try:
            query = r.recognize_google(audio)
            return query

        except sr.UnknownValueError:
            ttos.speak("not getting any voice")
            return "sorry"


def saysecondary():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        ttos.speak("any other instructionn you want me to do")
        print("im listening")

        audio = r.listen(source)  # record voice

        try:
            query = r.recognize_google(audio)
        except Exception:
            print("not getting any voice")
        print(query)
        return query


# features
def repeat():
    query = sayprime()
    if 'date' in query or 'time' in query:  # date and time
        resultdati = dateandtime.datentime(query)
        # print(resultdati)
        ttos.speak(resultdati)

    elif 'who' in query or 'what' in query:  # wikipedia search
        if 'who is' in query:
            query_search1 = query[7:]
            wiki_result = wiki.wi(query_search1)
            print(wiki_result)
            ttos.speak(wiki_result)
        else:
            query_search2 = query[8:]
            ttos.speak(wiki.wi(query_search2))


    elif "tell me a joke" in query or 'joke' in query:  # telling joke
        joke = pyjokes.get_joke(language='en', category='all')
        ttos.speak(joke)


    elif "take screenshot" in query or 'capture' in query:  # take screenshot
        ssc.sshot()
        ttos.speak("screenshot sucessfully taken")


    elif "how are you" in query or "how you doing" in query:
        ttos.speak("im good,how are you ")

    elif "search" in query:  # search in google
        google_search_query = query[7:]
        search_google.google_search(google_search_query)


    elif "sorry" in query:

        ttos.speak(print("this feature coming soon"))
    elif "no thanks " in query or "no" in query:
        print("okay")

    print("you want me to continue")
    permission = saysecondary()
    if permission == "yes" or permission == "yup":
        repeat()
    elif permission == 'no' or permission == 'nope':
        ttos.speak("thank you")
        return


repeat()
