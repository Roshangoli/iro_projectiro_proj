from flask import Flask, request, render_template
from indexer import Indexer

app = Flask(__name__)
indexer = Indexer()
indexer.load_index('index.pkl')

@app.route('/', methods=['GET'])
def search_page():
    return render_template('search.html')

@app.route('/query', methods=['POST'])
def handle_query():
    query_text = request.form['query']
    if not query_text:
        return render_template('search.html', results=None)
    results = indexer.query(query_text)
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
