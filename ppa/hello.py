from flask import Flask, render_template, request, escape, session
from vsearch import search4letters
from dbcm import UseDataBase
from checker import check_log_in

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'root',
                          'password': '',
                          'database': 'vsearchlogDB'}


def log_request(req: str, res):
    with UseDataBase(app.config['dbconfig']) as cursor:
        sql = """insert into logg
                 (phrase, letters, ip, browser_string, results)
                 values
                 (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (str(req.form['phrase']),
                             str(req.form['letters']),
                             str(req.remote_addr),
                             str(req.user_agent.browser),
                             str(res)))


@app.route('/search4', methods=['post', 'get'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title='Here are your results',
                           the_results=results,
                           the_phrase=phrase,
                           the_letters=letters)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on web')


@app.route('/view')
@check_log_in
def view() -> 'doc':
    with UseDataBase(app.config['dbconfig']) as cursor:
        sql = """select phrase, letters, ip, browser_string, results from logg"""
        cursor.execute(sql)
        data = cursor.fetchall()

    titles = ['Phrase', 'Letters', 'Remote_address', 'User_agent', 'Results']

    return render_template('view.html',
                           the_title='Viewer',
                           titles=titles,
                           data=data)


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return "you're now logged in"


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Say bye~'


app.secret_key = 'YouWillNeverGuessMySecrectKey'


app.run(debug=True)
