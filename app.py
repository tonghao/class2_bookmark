from flask import Flask, render_template

app = Flask(__name__)

bookmarks = [
    {'id': 1, 'title': 'Google', 'url': 'http://www.google.com'},
    {'id': 2, 'title': 'Yahoo', 'url': 'http://www.yahoo.com'},
    {'id': 3, 'title': 'bing', 'url': 'http://www.bing.com'},
]


@app.route('/')
def index():
    return render_template('index.html', bookmarks=bookmarks)


if __name__ == '__main__':
    app.run(debug=True)
