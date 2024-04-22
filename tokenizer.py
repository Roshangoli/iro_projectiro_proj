# tokenizer.py

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def custom_tokenizer(text):
    tokens = word_tokenize(text)
    english_stopwords = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in english_stopwords]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return lemmatized_tokens
