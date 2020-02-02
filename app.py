from flask import Flask, render_template, redirect, url_for, session, flash
from flask_moment import Moment
from datetime import datetime
from forms import UserForm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from threading import Thread
import os

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)
moment = Moment(app)
mail = Mail(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'ini-adalah-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cintakita@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = 'FLASK'
app.config['FLASK_MAIL_SENDER'] = 'kehilangan.info@gmail.com'
app.config['FLASK_ADMIN'] = os.environ.get('FLASK_ADMIN')


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

def  send_asyinc_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASK_MAIL_SENDER'], recipients=[kepada])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_asyinc_email, args=[app, msg])
    thr.start()
    return thr


@app.route('/', methods=['GET','POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():        
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASK_ADMIN']:
                send_email(app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ' '
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    form = UserForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Wow, kamu telah mengganti nama kamu!')
        session['name'] = form.nama.data
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


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Role=Role, User=User)
