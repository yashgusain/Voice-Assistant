import speech_recognition as sr
import texttospeech as ttos
import pyjokes
import search
import basic_feature


def sayprime():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        with open("name.txt","r+") as owner:
            greet=basic_feature.datentime('wish')+owner.read()+"how can i help you"
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
    if 'date' in query or 'tell me time' in query:
        try:
            resultdati = basic_feature.datentime(query)
            ttos.speak(resultdati)
        except TypeError:
            print(" ")

    # wikipedia search

    elif 'who' in query or 'what' in query:
        if 'who is' in query:
            query_searclang = query[7:]
            wiki_result = search.wi(query_searclang)
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


    elif "how are you"== query or"how you doing"== query:
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

    elif "no thanks " == query or "no" == query:
        print("okay")

    # app opening

    elif "open" in query:
        basic_feature.openapps(query)
        ttos.speak("opening app")
    elif "change name to" in query:
        name=query[15:]
        basic_feature.change_name(name)
        ttos.speak("name sucessfully changed")
    elif "remember that" in query:
        thing_to_remember=query[14:]
        basic_feature.remember_that(thing_to_remember)
        ttos.speak("sucessfully remembered")

    elif "read" in query:
        with open("journal.txt",mode="r") as reading:
            to_say="you said that"+reading.read()
            ttos.speak(to_say)
    elif "translate" in query:
        low=query.lower()
        lang= list(low.split(" "))
        language = lang[-1]
        language_short = language[0:2]

        removal_translate = lang.pop(0)
        removal_in = lang.pop(-2)
        removal_language = lang.pop(-1)
        complete_sentence = " ".join(lang)

        basic_feature.translating(complete_sentence,language_short,language)



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
