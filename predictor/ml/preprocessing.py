import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")


# Initialize NLP tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# Contractions used during training
contractions = {
    "i'm": "i am",
    "don't": "do not",
    "didn't": "did not",
    "it's": "it is",
    "i've": "i have",
    "you're": "you are",
    "can't": "cannot",
    "i'd": "i would",
    "that's": "that is",
    "isn't": "is not",
    "won't": "will not",
    "i'll": "i will",
    "we're": "we are",
    "they're": "they are"
}


def expand_contractions(text):
    text = text.split()
    text = [contractions.get(w, w) for w in text]
    return " ".join(text)


def clean_text(text, do_lemmatize=True, remove_stopwords=True):

    if not isinstance(text, str):
        return ""

    text = text.strip()
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\.\S+", " ", text)

    # Remove emails
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove mentions
    text = re.sub(r"@\w+", " ", text)

    # Remove hashtags
    text = re.sub(r"#\w+", " ", text)

    # Expand contractions
    text = expand_contractions(text)

    # Remove non-alpha characters
    text = re.sub(r"[^a-z\s']", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    tokens = nltk.word_tokenize(text)

    # Remove stopwords and single-character tokens
    if remove_stopwords:
        tokens = [
            t for t in tokens
            if t not in stop_words and len(t) > 1
        ]

    # Lemmatization
    if do_lemmatize:
        tokens = [
            lemmatizer.lemmatize(t)
            for t in tokens
        ]

    return " ".join(tokens)