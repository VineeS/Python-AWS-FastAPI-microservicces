import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is Wiki Fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """search wiki for names"""
    res = wikipedia.search(name)
    return res


def pharse(name):
    """Search for the phrases"""
    page = wiki(name)
    blob = TextBlob(page)

    return blob.noun_phrases
