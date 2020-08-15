# Template Engine

Pada bagian ini, kamu akan diberikan panduan bagaimana menggunakan template di Flask. Template sendiri berguna agar kita dapat merancang tampilan yang dapat digunakan berulang-kali _\(reusable\)_. Flask sendiri memiliki sendiri template engine yang disebut dengan nama Jinja2. Untuk mengetahui cara penggunaanya, silahkan lihat pada modul selanjutnya.

## Jinja Template Engine

Jinja2 adalah bahasa templating modern dan ramah desainer untuk Python, meniru model template Django atau Flask. Cepat, banyak digunakan, dan aman dengan lingkungan eksekusi template. Jinja2 digunakan di bagian Front end.

Contoh: Yang semula code HTML-nya seperti ini:

```markup
<h1>Hello, David</h1>
```

Setelah menggunakan Jinja2:

```markup
<h1>Hello, {{ name }} </h1>
```

Value dari `{{ name }}` akan dikirim melalui Route yang sudah kita pelajari sebelumnya.

### Rendering Template

Di bagian atas kamu mempunyai sebuah variable `{{ name }}` yang belum berisikan value. Disini di bagian Rendering Templates kamu akan akan memberikan value kepada `{{ name }}` dengan menuliskannya di bagian route:

```python
# app.py
from flask import Flask, render_template #tambahkan ini

#.........

# tambahkan kode dibawah ini
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
```

Dan jangan lupa untuk **membuat folder templates yang berisikan user.html** karna fungsi render\_template untuk membaca folder templates yang isinya user.html sehingga folder kamu terlihat seperti ini:

```bash
├── env/
|   └── .....
├── templates/
|   └── user.html
├── app.py
```

Dan buatlah kode seperti ini di dalam file user.html:

```markup
<h1>Hello, {{ name }}</h1>
```

dan cobalah untuk mengakses [https://127.0.0.1:5000/user/David](https://127.0.0.1:5000/user/David) di web browser kamu, maka hasilnya akan sama seperti sebelumnya, namun kamu berhasil menggunakan template pada pandua kali ini.

![http://127.0.0.1:5000/user/David](https://lh3.googleusercontent.com/Tz3yh7TeFr7SANXEKUkkhn7qnN42u3n-t0t2vJzC9oT592N7ayylIRFusU-gh5nxau4pGShOaJ5-KkG0MicB7vXpUc6RQVaOcWP246JGzvwCCHm3N78lbEUlpQu4DGgq4hVnxTTV)

### Variabel

`{{ name }}` adalah sebuah variabel. Namun, kamu juga harus tau bahwa di jinja2 ada fungsi untuk memfilter sebuah karakter namanya variabel filters contoh kecilnya seperti ini:

```markup
<h1>Hello, {{ name | capitalize }}</h1>
```

hasilnya akan membuat huruf awal dari variabel  menjadi kapital. Berikut ini adalah daftar beberapa variabel filter jinja:

| Nama Filter | Deskripsi |
| :--- | :--- |
| `safe` | Merender semua tags html |
| `capitalize` | Memberikan kapital pada huruf awal kalimat |
| `lower` | Membuat kalimat menjadi huruf kecil semua |
| `upper` | Membuat kalimat menjadi huruf besar semua |
| `title` | Membuat awal kata menjadi kapital |
| `striptags` | Menghilangkan tags html sebelum di rendering |

### Control Structure

Sekarang **kamu akan membuat file base.html di folder templates** dengan isi seperti kode dibawah ini:

```markup
# templates/base.html
<html>
<head>
    <title>{% block title %}{% endblock %} - My App</title>
</head>
<body>
{% block content %}
{% endblock %}
</body>
</html>
```

sehingga struktur direktori kamu menjadi seperti ini:

```bash
├── env/
|   └── .....
├── templates/
|   └── base.html
|   └── user.html
├── app.py
```

Di jinja2 juga kita bisa melakukan beberapa kontrol struktur seperti contoh kecilnya:

```markup
{% if name %}
<h1>Hello, {{ name }}</h1>
{% endif %}
```

Kemudian ubahlah di code kamu di bagian `user.html` menjadi seperti di bawah:

```markup
# templates/user.html
{% extends 'base.html' %}
{% block title %}Index{% endblock %}
{% block content %}
{% if name %}
    <h1>Hello, {{ name }}</h1>
{% endif %}
{% endblock %}
```

Jadi artinya extends ini adalah sebagai dasar template atau sebagai struktur dasar template yang diambil dari `base.html`. Jadi setiap block yang di `user.html` akan diposisikan sesuai block yang kamu tuliskan di `base.html`. Program kamu jadi lebih terstrukturkan!

Lalu coba jalankan kembali `flask run` dan pastikan program berjalan normal

![http://127.0.0.1:5000/user/David](https://lh6.googleusercontent.com/MstIFYYi91ArxWD89smH9rPt_1836Rj15uS8bQPE62_Iu8X5UKb56awHpPTI1oLlUr5Rm0IRHeb_zk00cQp224z1rqnQHVmcWck2mZmd3-ctozDGwVZ3FSmUnLZV1cJhT8U8BURL)

## Integrasi Bootstrap dengan Flask

#### Integrasi Bootstrap menggunakan CDN

Bootstrap membantu menciptakan antarmuka web menjadi lebih atraktif dan lebih bersih dan compatible dengan semua web browser baik desktop ataupun mobile, dan ini open-source. Di sesi ini kamu akan integrasikan bootstrap dengan web kamu dengan menggunakan CDN. Langkahnya seperti ini:

* Buka [https://getbootstrap.com/docs/4.4/getting-started/introduction/](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
* Copy dan Paste CDN CSS di bawah tag head pada `base.html` sehingga menjadi seperti ini

```markup
# templates/base.html
<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>{% block title %}{% endblock %} - My App</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

* Copy dan Paste juga CDN JS di atas `</body>` pada `base.html` sehingga kode lengkapnya seperti ini

```markup
# templates/base.html
<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>{% block title %}{% endblock %} - My App</title>
</head>
<body>
    {% block content %}{% endblock %}
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

Selanjutnya coba jalankan kembali `flask run` dan pastikan style pada tampilannya berubah

#### Menambahkan Navbar

Selanjutnya buatlah file baru pada folder templates dengan nama `navbar.html` sehingga struktur direktory kamu menjadi seperti ini:

```bash
├── env/
|   └── .....
├── templates/
|   └── base.html
|   └── navbar.html
|   └── user.html
├── app.py
```

Lalu tambahkan kode berikut ini pada `navbar.html`:

```markup
# templates/navbar.html
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
</nav>
```

`navbar.html` ini nanti berfungsi sebagai navbar kamu yang bisa kamu panggil secara terus menerus. Caranya tuliskan `{% include 'navbar.html' %}` dibawah tag body pada `base.html` sehingga seperti ini:

```markup
# templates/base.html
...
<body>
{% include 'navbar.html' %}
...
```

Kemudian kamu ubah:

```markup
...
{% if name %}
    <h1>Hello, {{ name }}</h1>
{% endif %}
...
```

yang ada di bawah `{% block content %}` pada `user.html` menjadi:

```markup
# templates/user.html
...
<div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-4">Hello, {{ name }}</h1>
  </div>
</div>
...
```

Sekarang kamu restart web browser kamu dan lihat perubahannya.

![http://127.0.0.1:5000/user/David](https://lh6.googleusercontent.com/fGIs-JODL1NXw2PlKS7hAhOUB6iThIukWrZwUfNMRr1nNt9szx6pkgwzvI6mMpDZAow6H6hRl8gg1CQTup7fdxXeVYP8wXdm-OjmXrbQfk0rTOuM7Nxw2lEy5_ZlwNbGYH2mK0aU)

## Kustom Halaman Error

Kustom Halaman Error adalah ketika kamu dalam mode `debug=False`/_\(Production\)_ dan terjadi error pada halaman website baik 404 _\(Not Found\)_, 403 _\(Forbidden\)_ ataupun 500 _\(Internal Server Error\)_. Agar terlihat lebih _user friendly_, kita dapat melakukan kustom pada halaman tersebut.

```python
# app.py
from flask import Flask, render_template
...
@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e)
    return render_template('500.html'), 500
```

`errorhandler` mengembalikan respon status kode 403, 404, dan 500. Jadi ketika terjadi error 404 maka akan mengakses halaman `404.html` dan seterusnya. Selanjutnya, kita akan membuat file template error `403.html`, `404.html`, `500.html` pada folder templates, sehingga struktur dari direktori nya akan terlihat seperti ini:

```bash
├── env/
|   └── .....
├── templates/
|   └── 403.html
|   └── 404.html
|   └── 500.html
|   └── base.html
|   └── navbar.html
|   └── user.html
├── app.py
```

**Status Kode 403**

```markup
# templates/403.html
{% extends 'base.html' %}
{% block title %}403 Forbidden{% endblock %}
{% block content %}
<div class="jumbotron jumbotron-fluid">
    <div class="container">
        <h1 class="display-4">403 Forbidden</h1>
    </div>
</div>
{% endblock %}
```

**Status Kode 404**

```markup
# templates/404.html
{% extends 'base.html' %}
{% block title %}404 Page Not Found{% endblock %}
{% block content %}
<div class="jumbotron jumbotron-fluid">
    <div class="container">
        <h1 class="display-4">404 Page Not Found</h1>
    </div>
</div>
{% endblock %}
```

**Status Kode 500**

```markup
# templates/500.html
{% extends 'base.html' %}
{% block title %}500 Internal Server Error{% endblock %}
{% block content %}
<div class="jumbotron jumbotron-fluid">
    <div class="container">
        <h1 class="display-4">500 Internal Server Error</h1>
    </div>
</div>
{% endblock %}
```

Error pages ini akan terbaca ketika kamu merubah `debug=False` nanti ketika mengakses halaman yang salah, akan muncul custome page `404.html` dan seterusnya.

![404 Not Found Ketika Mengakses Halaman Yang Salah](https://lh5.googleusercontent.com/K80u3y5zmUv18rAqtCyRIE0qfG8GN0ONOALO4lNDk37tcRJc2502d6GJ2p3DMBIVpwTq3YSrRUm5a1Ipb_Ifi5AT0Cq762hfi-V1gKSCQ1MHtZCJKYy2sRbUN2LEczbVmcjWB8g7)

 

![500 Internal Server Error Ketika Aplikasi Mengalami Error](https://lh4.googleusercontent.com/LkCSfyTfHylmlnVajEaY99jYI7o-jaYExfhT1Rayja3GEYXtkX3LbTpHFOoYglL7A9z32GyW07hjJsK0l6kD2E1FR9fMEKvCVnBD3imhNapnyV3nwYHMq-BcqQE_Q_rYNP-l4y4U)

## Link

Link digunakan untuk menghubungkan antara halaman, dalam flask untuk menghubungkan antar halaman kita dapat menggunakan `url_for`. `url_for` selain menghubungkan antar halaman, juga bisa digunakan untuk mengambil file dari gambar, css, js dan lainnya dari sebuah `Static Folder`.

Link yang akan kamu gunakan untuk menghubungkan antar halaman contohnya seperti ini:

```markup
<a href="{{ url_for('index') }}">Index</a>
```

**Penjelasannya**: `index` dalam `url_for` adalah nama fungsi dari route. Jadi ketika kamu ingin menghubungkan antar halaman, kamu harus memanggil fungsi routenya.

Tapi, jika dalam route itu membutuhkan sebuah nilai, contoh dalam route:

```python
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
```

jadi `url_for` menjadi seperti ini:

```markup
<a href="{{ url_for('user', name='David') }}">User David</a>
```

**Penjelasannya**: parameter name dengan nilai `David` akan dilempar ke dalam fungsi route yang bernama user.

Lalu bagaimana jika ingin mengambil file menggunakan `url_for`

```markup
<img src=”{{ url_for(‘static’, filename=’nama.jpg’) }}”/>
```

**penjelasannya**: 'static' dalam `url_for` adalah nama folder kamu, filename adalah nama filenya.

#### Contoh Penerapan

Dalam file `app.py` saat ini, terdapat 2 routes yang akan kita coba untuk saling hubungkan dengan cara seperti berikut:

Ubahlah kode yang ada pada `navbar.html` menjadi seperti ini:

```markup
<nav class="navbar navbar-light bg-light">
    <a class="navbar-brand" href="{{ url_for('index') }}">Navbar</a>
</nav>
```

Kemudian **buatlah sebuah file bernama `index.html`** didalam folder templates sehingga struktur direktori saat ini menjadi seperti ini:

```markup
├── env/
|   └── .....
├── templates/
|   └── 403.html
|   └── 404.html
|   └── 500.html
|   └── base.html
|   └── index.html
|   └── navbar.html
|   └── user.html
├── app.py
```

Lali isi kode `index.html` seperti ini:

```markup
{% extends 'base.html' %}
{% block title %}Index{% endblock %}
{% block content %}
<div class="jumbotron jumbotron-fluid">
    <div class="container">
        <a href="{{ url_for('user', name='David')}}" class="badge badge-pill badge-danger">User David</a>
    </div>
</div>
{% endblock %}
```

Selanjutnya ubah fungsi index pada route di `app.py` agar dapat melakukan render template ke file `index.html`

```python
# app.py
...
@app.route('/')
def index():
    return render_template('index.html')
...
```

Lalu coba jalankan server kembali untuk melihat hasil perubahannya.

![http://127.0.0.1:5000/](https://lh3.googleusercontent.com/la10D7Ri39-dxs2jtjBjGkeryCs-x76qWqvboJekf3I6ZJWppUxprTg7Hx1fgSwn1eGGchAgdCBpXFayxKGf2vmANCFic9TGGfURVMf4opRxeBQr8Y0-n5_WsCfs6hy9jDp47DWI)

## Tanggal & Jam dengan Flask Moment

Untuk mengatasi tanggal dan jam, flask menyediakan library yang bernama flask-moment. Didalam flask-moment terdapat javascript library yang disebut moment.js. Moment.js adalah javascript library yang bersifat open-source untuk merender tanggal dan waktu.

Kali ini kamu bakalan belajar cara menggunakan ekstensi flask, ini merupakan fitur yang disediakan flask agar mempermudah kita dalam menggunakan library yang sudah tersedia. Untuk menggunakan flask-moment cukup install flask-moment dengan menggunakan `pip` di terminal dan pastikan environment kamu saat ini aktif. Berikut ini cara menginstall flask moment:

```bash
(env) $ pip install flask-moment
```

Kemudian tambahkan kode seperti ini pada app.py untuk inisialisasi `flask-moment`

```python
# app.py: inisialisasi flask-moment
from flask import Flask, render_template
from flask_moment import Moment # Yang ditambahkan
from datetime import datetime # Yang ditambahkan

app = Flask(__name__)
moment = Moment(app) # Yang ditambahkan
...
```

kemudian pada fungsi route `user`, tambahkan parameter `current_time` yang menampung isi fungsi untuk menampilkan waktu saat ini:

```python
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())
```

Tambahkan kode ini di dalam `<head>` **pada base.html** agar flask-moment dapat digunakan:

```markup
# templates/base.html: menggunakan flask-moment
...
    {{ moment.include_jquery() }}
    {{ moment.include_moment() }}
    {{ moment.lang('id') }}
</head>
...
```

Lalu tambahkan juga kode berikut ini pada **user.html**

```markup
# templates/user.html: menambahkan format datetime
...
<p class="text-muted">{{ moment(current_time).format('LLLL') }}</p>
...
```

Sehingga kode lengkap nya akan menjadi seperi ini:

```markup
{% extends 'base.html' %}
{% block title %}Index{% endblock %}
{% block content %}
<div class="jumbotron jumbotron-fluid">
    <div class="container">
      <h1 class="display-4">Hello, {{ name }}</h1>
      <p class="text-muted">{{ moment(current_time).format('LLLL') }}</p>
    </div>
</div>  
{% endblock %}
```

Lalu akses kembali halaman [https://127.0.0.1:5000/user/David](https://127.0.0.1:5000/user/David) untuk melihat hasil perubahannya.

![http://127.0.0.1:5000/user/David](https://lh3.googleusercontent.com/yugtKPvLg4BGHSX401VPnSSYiWQM2cvuZax2CJYJZUBY3PO1rqxUg1fLsossNc978btMIkSrq9rmY2YJCX5FJftA1g-bnbMtaWk9IW26HpRyBMGEM_4S2VtKFgYvRM9KMcSmF0GR)

Selengkapnya untuk format waktu & tanggal pada Flask-Moment

| Format | Hasil |
| :--- | :--- |
| .format\('L'\) | 17/01/2020 |
| .format\('LL'\) | 17 Januari 2020 |
| .format\('LLL'\) | 17 Januari 2020 pukul 10.10 |
| .format\('LLLL'\) | Jumat, 17 Januari 2020 pukul 10.10 |
| .fromNow\(\) | 7 menit yang lalu |
| .calendar\(\) | 17/01/2020 |

## Web Forms Menggunakan Flask WTF

Dengan HTML, memungkinkan kamu untuk membuat web forms, dimana user bisa memasukkan informasi melalui web browser ke server dan biasanya menggunakan method adalah POST. Dengan Form HTML biasa sebenarnya kamu sudah bisa mengambil nilai dari form dengan `request.form`, namun dengan flask-wtf kamu bisa melakukan validation form dan dapat menggunakan kembali kode tersebut _\(reusable\)_. Cara install ekstensi flask-wtf cukup dengan cara:

```bash
(env) $ pip install flask-wtf
```

ketika sudah selesai menginstall terdapat dua paket yang terinstal yaitu Flask-WTF dan WTForms.

### Konfigurasi Flask WTF

Tidak seperti kebanyakan ekstensi, flask-wtf tidak perlu untuk kamu inisialisasi. Kamu cuma perlu untuk melakukan konfigurasi di `app.py`. Konfigurasi ini berupa `secret_key` yang artinya hanya kamu sendiri yang tau secret\_key ini. Kamu bisa melakukan configurasi seperti ini pada `app.py`

```python
# app.py: konfigurasi forms
...
app = Flask(__name__)
moment = Moment(app)
app.config['SECRET_KEY'] = 'this-secret-not-enough' # tambahkan kode ini
...
```

### Kelas Form

Ketika menggunakan flask-wtf, masing-masing dari form yang berada di web diwakili oleh kelas FlaskForm. Setiap field form boleh memiliki validator lebih dari satu. Validator adalah fungsi yang memeriksa apakah data yang dikirimkan oleh pengguna valid atau tidak valid.

Tambahakan kode ini pada `app.py`

```python
# app.py: menambahkan forms
...
# Forms - Tambahkan kode ini
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
moment = Moment(app)
app.config['SECRET_KEY'] = 'thisisverysecret'

# Forms - Tambahkan kode ini
class UserForm(FlaskForm):
    name = StringField('Siapa nama kamu?', validators=[DataRequired()])
    submit = SubmitField('Lanjutkan')

...
```

Berikut ini tipe field pada Flask-WTF:

| Tipe Field | Deskripsi |
| :--- | :--- |
| BooleanField | True dan False |
| DateField | Text Field untuk datetime.date |
| DateTimeField | Text Field untuk datetime.datetime |
| DecimalField | Text Field untuk decimal.Decimal |
| FileField | Untuk upload file |
| HiddenField | Hidden text field |
| MultipleFileField | Untuk upload banyak file |
| FieldList | List untuk field |
| FloatField | Text Field untuk float |
| FormField | Form embedded sebagai field |
| IntegerField | Text Field untuk integer |
| PasswordField | Text Field untuk password |
| RadioField | List radio button |
| SelectField | Dropdown list |
| SelectMultipleField | Dropdown list untuk memilih lebih dari 1 |
| SubmitField | Button submit |
| StringField | Text Field untuk string |
| TextAreaField | Text Area |

Dan tipe-tipe data untuk wtforms.validators:

| Validator | Deskripsi |
| :--- | :--- |
| DataRequired | Field tidak boleh kosong |
| Email | Validasi email address |
| EqualTo | Membandingkan nilai dari dua field |
| InputRequired | Field tidak boleh kosong |
| IPAddress | Validasi untuk IPv4 network address |
| Length | Validasi panjang karakter |
| MacAddress | Validasi MacAddress |
| NumberRange | Validasi panjang panjang numeric |
| Optional | Memberikan nilai kosong pada field |
| Regexp | Memvalidasi input terhadap ekspresi reguler |
| URL | Validasi URL |
| UUID | Validasi UUID |
| AnyOf | Memvalidasi bahwa input adalah salah satu dari daftar nilai yang mungkin |
| NoneOf | Memvalidasi bahwa input adalah tidak ada dari daftar nilai yang mungkin |

### Rendering HTML Form

Form yang sudah kamu buat pada `app.py` bisa kamu gunakan di template kamu dengan cara:

```markup
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }}
    {{ form.name() }}
    {{ form.submit() }}
</form>
```

Kode di atas kamu tambahan class buat bootstrap dan tambahkan kode tersebut ke `index.html` sehingga seperti di bawah ini:

```markup
# templates/index.html: menambahkan forms
...
<div class="container">
    <a href="{{ url_for('user', name='David') }}" class="badge badge-pill badge-danger">User David</a>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div class="form-group row">
            {{ form.name.label(class="col-sm-4 col-form-label") }}
            <div class="col-sm-8">
                {{ form.name(class="form-control") }}
            </div>
        </div>
        {{ form.submit(class="btn btn-block btn-primary") }}
    </form>
</div>
...
```

Karna di `index.html` kita menggunakan form dengan method POST tentunya kita juga akan menambahkan method pada route `index` dan juga paramater form untuk di panggil pada `index.html`

```python
# app.py: menambahkan method dan parameter form
...
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    return render_template('index.html', form=form)
...
```

Cobalah akses [http://127.0.0.1:5000](http://127.0.0.1:5000)

![http://127.0.0.1:5000](https://lh3.googleusercontent.com/29_sgHJfK8_313SRQ-fBJyPnbU3GGxLfCQw7H4VDi7vK_s7ffwGjqfMAMoN4mhgT63wPPU6s26gsJQATfPFjn1xVjQ1pS9Ze7Tnm8vlB0FR90IYHoAgZ1W6_irh5Ub6rPbMVpBp4)

### Form Handling di Fungsi Views Dan Menggunakan Redirect

Pada sesi ini kamu akan mempelajari bagaimana melempar nilai dari form melalui route, ubah kode kamu menjadi seperti ini:

```python
# app.py: menambahkan redirect dan url_for
from flask import Flask, render_template, redirect, url_for
from flask_moment import Moment
...

@app.route('/', methods=['GET', 'POST')
def index():
    form = UserForm()
    if form.validate_on_submit(): # tambahkan ini
        name = form.name.data # tambahkan ini
        return redirect(url_for('user', name=name)) # tambahkan ini
    return render_template('index.html', form=form)
...
```

**Penjelasan:** Kamu tambahkan methods GET dan POST agar data yang kita inputkan pada form bisa di ambil dan di post pada variabel nama. `form.validate_on_submit()` berfungsi untuk memvalidasi dari isi formnya, kosong atau tidak. Return redirect berfungsi ketika form berhasil di isi halamannya akan langsung ke redirect ke route user dengan membawa variabel nama.

Lalu coba jalankan [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

![Redirect ke halaman beranda setelah mengisi nama di form](https://lh3.googleusercontent.com/mv90l46kBRUjnRDUn9lYlDYRP6XLZLFQUiYS53fDrpS-R0iGFndITlT4YzErWRbpvHBAMKxzsFbugAfU1iXz1WRC-qUqyL87KmA12zya-k-XMw4mSIH8h2q_Em9o5cvHqXmRutRC)

### Pesan Flashing

Pesan flashing disini berfungsi untuk ketika kamu berhasil menginputkan value dengan benar maka akan memberikan pesan ke sisi client \(template\). Caranya penggunaanya seperti ini:

```python
# app.py: menambahkan flash
from flask import Flask, render_template, url_for, redirect, session, flash
...

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        old_name = session.get('name') # tambahkan ini
        if old_name is not None and old_name != form.name.data:  # tambahkan ini
            flash('Wow, anda telah mengganti nama anda!')  # tambahkan ini
        session['name'] = form.name.data
        return redirect(url_for('user', name=session.get('name')))
    return render_template('index.html', name=session.get('name'), form=form)
...
```

Dan tambahkan `flash message` pada bagian client, caranya tambahkan kode ini pada `base.html` di bawah `{% include 'navbar.html' %}` dan di atas `{% block content %}`:

```markup
...
# base.html
...
{% include 'navbar.html' %}
{% for message in get_flashed_messages() %}
<div class="alert alert-warning alert-dismissible fade show mb-0" role="alert">
  {{ message }}
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>
{% endfor %}
{% block content %}{% endblock %}
...
```

### User Sessions

Sebelum menggunakan session sebaiknya kamu mengetahui apa itu session. Session hampir mirip dengan cookie, perbedaannya yaitu jika cookie disimpan di browser namun session disimpan di sisi server, serta data session yang disimpan akan hilang apabila user telah meninggalkan server tersebut \(tutup browser\). Jadi session dapat diartikan tempat menyimpan data yang disimpan didalam server, yang data tersebut akan hilang apabila user telah meninggalkan server, atau dalam konteks ini user telah menutup browser. Karena data session disimpan pada server maka session lebih aman untuk menyimpan data-data penting bila dibandingkan dengan cookie, cara menggunakannya sebagai berikut:

Ubahlah kode `app.py` kamu hingga seperti ini:

```markup
# app.py: menggunakan session
from flask import Flask, render_template, url_for, redirect, session
...

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('user', name=session.get('name')))
    return render_template('index.html, form=form, name=session.get('name')
...
```

Ubahlah kode `index.html` sebagai berikut:

```markup
# templates/index.html: merubah link name='David'
...
<div class="container">
    {% if name %}
    <a href="{{ url_for('user', name=name) }}" class="badge badge-pill badge-danger">User {{ name }}</a>
    {% endif %}
    <form method="POST">
    ...
</div>
...
```

Memberikan kondisi ke template kamu karena ketika session `name` tidak lagi tersimpan di sisi server, maka link yang di dalam kondisi tidak dijalankan. Dan ketika kamu menginputkan nama kamu. Secara otomatis nilai dari form name akan tersimpan di session.

Akseslah halaman [http://127.0.0.1:5000/user/David](http://127.0.0.1:5000/user/David) untuk melihat perubahannya.

![http://127.0.0.1:5000/user/David](https://lh6.googleusercontent.com/Aj-2MQsZgEjQSG_L16j_fB2Xxd2rGWRtMlATuCD47WZGbJQx3uqmcTpdHu4lcQ5q_4NwlKshqXt7z4-P8n1AjWaOZ1D0C1EhBRuaTxsrXuopGpKohRtjB0yvXqBfVQyEplppjLEd)

