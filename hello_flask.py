from flask import Flask, render_template
from vsearch import search4letters


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from flask!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru!'))


@app.route('/entry')
def entry_page() -> str:
    return render_template('entry.py', the_title='WEB版のserch4lettersにようこそ！')


app.run()
