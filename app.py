from project import app,db
from flask import render_template,url_for, redirect, flash, request
from project.forms import RegistrationForm, LoginForm
from project.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, UserMixin, current_user

@app.route('/', methods= ['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods= ['GET', 'POST'])
def login():

    form  = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invaid email or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))


    return render_template('login.html', form = form)

@app.route('/signup', methods= ['GET', 'POST'])
def signup():
    form  = RegistrationForm()
    if request.method == "POST":
        password = form.password.data
        password_hash = generate_password_hash(password)
        
        user = User(
            names = form.names.data,
            email = form.email.data,
            password_hash = password_hash
        )

        db.session.add(user)
        db.session.commit()
        flash("registration was successful", "success")
        return redirect(url_for('login'))

    
    return render_template('signup.html', form = form )
 