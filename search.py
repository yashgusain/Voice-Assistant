import webbrowser as wb
import wikipedia as wiki
import search


def google_search(query):
        search = query
        search.replace(" ", "+")
        return wb.open(
            "https://www.google.com/search?sxsrf=ALeKk01BD6AglxCcg54Xt0IE5sKU1pTDkw%3A1607436721145&ei=sYnPX_6tCMz39QOW74iIBA&q=" + search + "&oq=" + search + "&gs_lcp=CgZwc3ktYWIQAxgAUABYAGAkaABwAHgAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab")

def  youtube_search(query):
    yt = query
    yt.replace(" ", "+")
    return wb.open("https://www.youtube.com/results?search_query=" + query)

def wi(topic):
    try:
        wiki.summary(sentences=1, title=topic)
        return wiki.summary(sentences=1, title=topic)
    except wiki.exceptions.DisambiguationError:
        return search.google_search(topic)