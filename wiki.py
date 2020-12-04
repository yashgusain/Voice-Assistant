import wikipedia as wiki


def wi(topic):
    try:
        wiki.summary(sentences=1, title=topic)
        return wiki.summary(sentences=1, title=topic)
    except wiki.exceptions.DisambiguationError:
        return "please be more specific"
