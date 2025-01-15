import nltk


def init_nltk_modules():
    if not nltk.data.find("stopwords"):
        nltk.download("stopwords")

    if not nltk.data.find("wordnet"):
        nltk.download("wordnet")

    if not nltk.data.find("omw-1.4"):
        nltk.download("omw-1.4")
