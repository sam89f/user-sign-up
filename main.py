from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup', methods=['POST', 'GET'])
def user_signup():

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    username = ''
    password = ''
    verify = ''
    email = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        
        if verify != password:
            verify_error = 'Verified password and password must match'
            password = ''
            verify = ''

        if len(username) < 3:
            username_error = 'Username must at least three characters'
            username = ''
            password = ''
            verify = ''

        if not username_error and not password_error and not verify_error and not email_error:
            user = username
            return redirect('/verified?user={0}'.format(user))

    return render_template('signup.html', title='User signup',username=username, username_error=username_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error)

@app.route('/verified')
def user_verified():
    user = request.args.get('user')
    return render_template('verified.html', User=user)


app.run()