from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

bookmarks = [
    {'id': 1, 'title': 'Google', 'url': 'http://www.google.com'},
    {'id': 2, 'title': 'Yahoo', 'url': 'http://www.yahoo.com'},
    {'id': 3, 'title': 'bing', 'url': 'http://www.bing.com'},
]

users = [
    {"username": "admin", "password": "admin"},
    {"username": "user1", "password": "user1"},
]


@app.route('/')
def index():
    return render_template('index.html', bookmarks=bookmarks)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 用户验证
        return redirect(url_for("index"))
    return render_template('login.html')


@app.route('/logout')
def logout():
    return "logout"


@app.route('/register')
def register():
    return "register"


@app.route('/add_bookmark', methods=['GET', 'POST'])
def add_bookmark():
    if request.method == 'POST':
        title = request.form['title']
        url = request.form['url']
        if not url.startswith('http'):
            url = "https://" + url
        id = bookmarks[-1]['id'] + 1

        # 保存数据
        bookmark = {"title": title, "url": url, "id": id}
        bookmarks.append(bookmark)

        return redirect(url_for('index'))
    return render_template('add_bookmark.html')


if __name__ == '__main__':
    app.run(debug=True)
