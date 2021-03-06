# Menggunakan Email

Banyak hal bisa terjadi dari sisi client dan server yang bisa dikomunikasikan dengan email.

## Support Menggunakan Flask Mail

Paket smtplib dari python library bisa digunakan untuk mengirim email menggunakan aplikasi flask, paket smtplib dibungkus dalam extensi `flask-mail` dan terintegrasi dengan baik dalam flask.

```text
(env) $ pip install flask-mail
```

`flask-mail` terhubung ke server Simple Mail Transfer Protocol \(SMTP\) dan mengirim email kepada penerima. Nah, jika kamu tidak mengkonfigurasi flask-mail terhubung ke localhost dan otomatis portnya 25 tanpa otentikasi.

Flask-Mail SMTP Configuration Keys

| Key | Default | Description |
| :--- | :--- | :--- |
| `MAIL_SERVER` | localhost | Hostname or IP address |
| `MAIL_PORT` | 25 | Port email server |
| `MAIL_USE_SSL` | False | Enable TLS security |
| `MAIL_USE_TLS` | False | Enable SSL security |
| `MAIL_USERNAME` | None | Username email |
| `MAIL_PASSWORD` | None | Password email |

Cara menggunakannya, tuliskan pada app.py:

```python
# app.py: konfigurasi email
...
import os

...
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
```

dan lakukan juga inisialisasi flask-mail pada app.py:

```python
# app.py: inisialisasi flask-mail
...
from flask_mail import Mail
...

mail = Mail(app)
...
```

Dua variabel untuk email username dan email password perlu diexport melalui environment. 

**Linux or MacOS:**

```text
(env) $ export MAIL_USERNAME='gmail username'
(env) $ export MAIL_PASSWORD='gmail password'
```

**Windows**

```text
(env) $ set MAIL_USERNAME='gmail username'
(env) $ set MAIL_PASSWORD='gmail password'
```

**T**api, sebelum kamu menggunakan email kamu untuk mengirim email. Enable less secure gmail kamu dengan masuk ke link [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps).

## Mengirim Email Dari Python Shell

**Jalankan flask shell pada terminal:**

```text
(env) $ flask shell
>>> from flask_mail import Message
>>> from app import mail
>>> msg = Message(‘Ngetest Email’, sender=’emailkamu@gmail.com’, recipients=[‘penerima@gmail.com’])
>>> msg.body = ‘Body’
>>> msg.html = ‘<b>HTML</b> body’
>>> from flask import current_app
>>> with app.app_context():
. . . 	mail.send(msg)
```

Metode `send()` menggunakan `current_app` sehingga perlu dijalankan dengan `app_context` yang di aktifkan.

## Integrasi Email Dengan Aplikasi

Untuk membuat email ini dikirim secara otomatis, maka kamu harus menuliskan fungsionalitas pengiriman email ke dalam suatu fungsi. 

```python
# app.py: integrasi email dengan app
from flask_mail import Message

app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[FLASK]'
app.config['FLASK_MAIL_SENDER'] = 'nama_pengirim@gmail.com'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config[‘FLASK_MAIL_SUBJECT_PREFIX’] + subject, sender=app.config['FLASK_MAIL_SENDER'], recipient=[penerima])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
```

Fungsi ini bergantung pada 2 kunci konfigurasi `FLASK_MAIL_SUBJECT_PREFIX` sebagai awalan dan `FLASK_MAIL_SENDER` sebagai alamat pengirim. Fungsi `send_email` mengambil alamat `to, subject, template` Nama template harus tanpa ekstensi, sehingga 2 versi template dapat digunakan untuk teks biasa \(plain text\) dan HTML.

Fungsi `index()` dapat diperluas fungsinya menjadi ketika menerima nama baru maka akan mengirim email ke administrator. Rubahlah kode pada fungsi `index()` menjadi seperti ini:

```python
# app.py: menambahkan ke route
#........
app.config['FLASK_ADMIN'] = os.environ.get('FLASK_ADMIN')

app.route('/', methods=['GET','POST'])
def index():
	form = UserForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			db.session.commit()
			flash(‘Senang bertemu kamu’)
			if app.config['FLASK_ADMIN']:
				send_email(app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=user)
		else:
			flash('Eh, kita ketemu lagi dong')
		session['name'] = form.name.data
		return redirect(url_for('user', name=session.get('name')))
	return render_template('index.html', form=form, name=session.get('name'))

```

Penerima email adalah `FLASK_ADMIN` dalam variabel konfigurasi. Dua file template perlu dibuat untuk versi plain text dan HTML. File-file ini perlu disimpan dalam subdirektori mail di dalam template untuk memisahkannya dari template biasa.

Dalam kasus sebelum-sebelumnya, kamu harus export environment variabel `FLASK_ADMIN` agar bisa digunakan :

**Linux/MacOs**

```bash
(env) $ export FLASK_ADMIN=<your-email-address>
```

**Windows**

```bash
(env) $ set FLASK_ADMIN=<your-email-address>
```

## **Mengirim Email Secara** Asynchronous

Jika kamu mengirim beberapa email, kemungkinan membuat browser terlihat tidak responsif selama beberapa saat. Untuk menghindari keterlambatan yang tidak perlu selama penanganan permintaan, fungsi `send_email()` dapat dipindahkan seperti ini dibawah `app.config`:

```python
# app.py: menambahkan asynchronus email
from threading import Thread

def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(to, subject, template, **kwargs):
	msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASK_MAIL_SENDER'], recipient=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr
```

Kamu perlu sebuah template untuk menampung msg.body dan msg.html, untuk kamu harus membuat sebuah file di dalam template:

```python
# templates/mail/new_user.txt: menambahkan template body
Ada user baru
```

```markup
# templates/mail/new_user.html: menambahkan template html
<p>Ada user <strong><i>{{ user.username }}</i></strong> yang terdaftar dalam database</p>
```

Ketika ada nama user baru yang diinputkan, secara otomatis kamu akan menerima email tentang hal tersebut. Dan fungsi `flask_mail` `send()` menggunakan `current_app`,  jadi itu membutuhkan `app_context()` untuk mengaktifkannya. Jika kamu menjalankannya sekarang aplikasinya jauh lebih responsif. Fungsi `send_async_email()` dapat dikirim ke antrian tugas. Masalahnya sekarang adalah script `app.py` menjadi lebih besar dan itu membuatnya lebih sulit untuk dikerjakan. Dalam selanjutnya, kamu akan belajar caranya menyusun aplikasi yang lebih besar.



