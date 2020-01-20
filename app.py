from flask import Flask, render_template, redirect, url_for, session, flash
from flask_moment import Moment
from datetime import datetime
from forms import User
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ini adalah secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cintakita@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
moment = Moment(app)

@app.route('/', methods=['GET','POST'])
def index():
    form = User()
    if form.validate_on_submit():        
        session['nama'] = form.nama.data
        return redirect(url_for('user', name=session.get('nama')))
    return render_template('index.html', form=form, name=session.get('nama'))

@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    form = User()
    if form.validate_on_submit():
        old_name = session.get('nama')
        if old_name is not None and old_name != form.nama.data:
            flash('Wow, kamu telah mengganti nama kamu!')
        session['nama'] = form.nama.data
        return redirect(url_for('user', name=session.get('nama')))
    return render_template(
        'user.html', 
        name=session.get('nama'),
        current_time=datetime.now(), form=form
        )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

