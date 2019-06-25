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
        
        if len(username) < 3 or len(username) > 20 or ' ' in username:
            username_error = 'Username must be between 3 and 20 characters and contain no spaces.'
           

        if len(password) < 3 or len(password) > 20 or ' ' in password:
            password_error = 'Passward must be between 3 and 20 characters and contain no spaces.'
            

        if verify != password:
            verify_error = 'Verified password and password must match.'

        if  email and (not '@' in email and not '.' in email or ' ' in email or len(email) < 3 or len(email) > 20):
            email_error = "Email must be between 3 and 20 characters, and must contain '@' or '.' character, and no spaces."
             
        if username_error:
            username = ''
            password = ''
            verify = ''

        if password_error:
            password = ''
            verify = ''
        
        if verify_error:
            password = ''
            verify = ''

        if email_error:
            email = ''
            password = ''
            verify = ''

        if not username_error and not password_error and not verify_error and not email_error:
            user = username
            return redirect('/verified?user={0}'.format(user))

    return render_template('signup.html', title='User signup',username=username, username_error=username_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error)

@app.route('/verified')
def user_verified():
    user = request.args.get('user')
    return render_template('verified.html', User=user, title='User verified!')


app.run()