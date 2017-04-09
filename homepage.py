"""
Alisha Pegan Flask Toolbox
Web page that ask for the user to fill a form, checks if data was
provided, and then displays the results.
"""

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


def login():
    if request.method == 'GET':
        start = request.form['start']
        end = request.form['end']
        assault = request.form['assault']
        kidnap = request.form['kidnap']
        caraccident = request.form['caraccident']
        murder = request.form['murder']
        radius = request.form['radius']
        if start and end:
            return render_template('login.html',
                                   start=start, end=end)
        else:
            return redirect(url_for('error'))


@app.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'POST':
        return redirect(url_for('homepage'))
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
