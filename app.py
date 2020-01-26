from flask import Flask, render_template, redirect, url_for, session, flash
from flask_moment import Moment
from datetime import datetime
from forms import UserForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ini adalah secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cintakita@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
moment = Moment(app)

class Role(db.Model):
    __tablename__ = 'roles'

    id  = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(64), unique=True)
    users   = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role {}>'.format(self.name)

class User(db.Model):
    __tablename__ = 'users'

    id  = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)


@app.route('/', methods=['GET','POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():        
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.nama.data = ' '
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    form = User()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Wow, kamu telah mengganti nama kamu!')
        session['nama'] = form.nama.data
        return redirect(url_for('user', name=session.get('name')))
    return render_template(
        'user.html', 
        name=session.get('name'),
        current_time=datetime.now(), form=form
        )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

