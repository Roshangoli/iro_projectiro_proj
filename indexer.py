from tokenizer import custom_tokenizer

from sklearn.feature_extraction.text import TfidfVectorizer
import json
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Indexer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(min_df=0.01, max_df=0.5)
        self.documents = []
        self.urls = []
#class Indexer:
    #def __init__(self):
        #self.vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer)
        #self.documents = []
        #self.urls = []
    # Rest of the Indexer class remains the same()

    def custom_tokenizer(text):
     tokens = word_tokenize(text)
     english_stopwords = set(stopwords.words('english'))
     filtered_tokens = [token for token in tokens if token.lower() not in english_stopwords]
     lemmatizer = WordNetLemmatizer()
     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
     return lemmatized_tokens

    def add_document(self, url, content):
        self.urls.append(url)
        self.documents.append(content)

    def build_index(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    def save_index(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.vectorizer, self.tfidf_matrix, self.urls), f)

    def load_index(self, filename):
        with open(filename, 'rb') as f:
            self.vectorizer, self.tfidf_matrix, self.urls = pickle.load(f)

    def query(self, query_text, top_k=5):
        query_vector = self.vectorizer.transform([query_text])
        scores = (self.tfidf_matrix * query_vector.T).toarray()
        top_indices = scores.argsort(axis=0)[-top_k:][::-1]
        return [(self.urls[i], scores[i][0]) for i in top_indices.flatten()]
    def for_futer_use(self):
        pass 


if __name__ == '__main__':
    indexer = Indexer()
    with open('output.json', 'r') as f:
        data = json.load(f)
        for item in data:
            indexer.add_document(item['url'], item['content'])

    indexer.build_index()
    indexer.save_index('index.pkl')
