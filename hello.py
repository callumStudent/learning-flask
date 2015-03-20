from flask import Flask, url_for
app = Flask(__name__)

@app.route('/profile/<username>')
def show_user_profile(username):
    return 'User: {}'.format(username)

@app.route('/')
def show_url_for():
    return url_for('show_user_profile', username='callum') 

if __name__ == '__main__':
    app.debug = True
    app.run()
