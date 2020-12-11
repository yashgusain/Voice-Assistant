import speech_recognition as sr
import texttospeech as ttos
import pyjokes
import search
import basic_feature


def sayprime():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        with open("name.txt","r+") as owner:
            greet=basic_feature.datentime('wish')+owner.read()
            ttos.speak(greet)
        print("im listening")

        audio = r.listen(source)  # record voice

        try:
            query = r.recognize_google(audio)
            print(query)
            return query

        except sr.UnknownValueError:
            ttos.speak("not getting any voice")


def saysecondary():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        ttos.speak("any other instructionn you want me to do")
        print("im listening")

        audio = r.listen(source)  # record voice

        try:
            query = r.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            ttos.speak("not getting any voice")



# features
def repeat():
    query = sayprime()

    # date and time
    if 'date' in query or 'time' in query:
        try:
            resultdati = basic_feature.datentime(query)
            ttos.speak(resultdati)
        except TypeError:
            print(" ")

    # wikipedia search

    elif 'who' in query or 'what' in query:
        if 'who is' in query:
            query_search1 = query[7:]
            wiki_result = search.wi(query_search1)
            print(wiki_result)
            ttos.speak(wiki_result)
        else:
            query_search2 = query[8:]
            ttos.speak(search.wi(query_search2))

    # telling joke

    elif "tell me a joke" in query or 'joke' in query:
        joke = pyjokes.get_joke(language='en', category='all')
        ttos.speak(joke)

    # take screenshot

    elif "take screenshot" in query or 'capture' in query:
        basic_feature.sshot()
        ttos.speak("screenshot sucessfully taken")


    elif "how are you"in query or"how you doing"in query:
        ttos.speak("im good,how are you ")

    # Google and Youtube search

    elif "search" in query:  # search in google
        google_search_query = query[7:]
        search.google_search(google_search_query)
    elif "videos of " in query:
        yt = query[10:]
        search.youtube_search(yt)

    elif "sorry" in query:

        ttos.speak(print("this feature coming soon"))

    elif "no thanks " in query or "no" in query:
        print("okay")

    # app opening

    elif "open" in query:
        basic_feature.openapps(query)
        ttos.speak("opening app")
    elif "change name to" in query:
        name=query[14:]
        basic_feature.change_name(name)
        ttos.speak("name sucessfully changed")


    print("you want me to continue")
    permission = saysecondary()
    if permission == "yes" or permission == "yup":
        repeat()
    elif permission == 'no' or permission == 'nope':
        ttos.speak("thank you")
    else:
        pass


try:
    repeat()
except TypeError:
    pass
