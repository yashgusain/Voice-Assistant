import wikipedia as wiki
import search_google



def wi(topic):
    try:
        wiki.summary(sentences=1, title=topic)
        return wiki.summary(sentences=1, title=topic)
    except wiki.exceptions.DisambiguationError:
        return search_google.google_search(topic)

