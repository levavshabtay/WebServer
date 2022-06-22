from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

# instagram link
@app.route('/insta')
def insta():
    return redirect("https://www.instagram.com/bengurionuniversity/?hl=en")


# facebook link
@app.route('/facebook')
def facebook():
    return redirect("https://www.facebook.com/BenGurionUniversity/")


# root of study buddy website
@app.route('/')
def index_func():
    return render_template('homepage.html')


# root of contact us
@app.route('/connect')
def connect_func():
    return render_template('connect.html')


# root of about -- ass 3_1
@app.route('/about')
def about_page():
    user_info = {'user_name': 'levav', 'second_name': 'shabtay', 'nick_name': 'lev',
                 'study': 'engineering'}
    hobbies = ('makeUp', 'dance', 'movies', 'TV', 'food making', 'sport')
    session['CHECK'] = 'about'
    return render_template('assignment3_1.html',
                           user_info=user_info,
                           hobbies=hobbies)


# root of users - ass 3_2
@app.route('/users', methods=['GET', 'POST'])
def users_page():
    # search form - get method
    if request.method == 'GET':
        if 'email' in request.args:
            email = request.args['email']
            if email in user_dict:
                return render_template('assignment3_2.html',
                                       name=user_dict[email][0],
                                       email=email,
                                       nickName=user_dict[email][1])
            if len(email) == 0:
                return render_template('assignment3_2.html',
                                       user_dict=user_dict)
            else:
                return render_template('assignment3_2.html', message1='sorry, User not exist ')

    # Post Case
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        nickName = request.form['nickName']
        if email in user_dict:
            session['logedin'] = False
            return render_template('assignment3_2.html',
                                   message2='Hey there, you already registered!')
        else:
            session['username'] = username
            session['email'] = email
            session['nickName'] = nickName
            session['logedin'] = True
            user_dict[email] = (username, nickName)
            return render_template('assignment3_2.html')

    else:
        return render_template('assignment3_2.html')


@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('users_page'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))


user_dict = {
    'Levavs@gmail.com': ['Levav', 'levi'],
    'Benny@gmail.com': ['Benny', 'benjy'],
    'Tati@gmail.com': ['Tatiana', 'tati'],
    'Noam@gmail.com': ['Noam', 'nona'],
    'LinoyA@gmail.com': ['Linoy', 'lin']
}


if __name__ == '__main__':
    app.run(debug=True)
