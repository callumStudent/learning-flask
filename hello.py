from flask import Flask, request, render_template, redirect, url_for, flash, session
import logging
from logging.handlers import RotatingFileHandler
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
	if valid_login(
		request.form.get('username'),
		request.form.get('password')
	):
	    flash("Successfully logged in")
	    session['username'] = request.form.get('username')
	    return redirect(url_for('welcome'))
	else:
	    error = "Incorrect username or password"
	    app.logger.warning(
		    "Incorrect username or password for user ({})".format(
			request.form.get("username")))
    return render_template('login.html', error=error)

@app.route('/')
def welcome():
    if 'username' in session:
	return render_template('welcome.html', username=session['username'])
    else:
	return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def valid_login(username, password):
    # checks on the db if the username and password are correct
    if username == password:
	return True
    else:
	return False

if __name__ == '__main__':
    app.secret_key = 'dc\xd8T\xb6O\xf3\xf3\xf7\xc1k\xcft\xe9qdk\xaa\xa0\xbbn+\x0cX'
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.debug = True
    app.run()
