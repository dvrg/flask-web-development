# Python Packages

Python Packages akan terpasang bersamaan dengan pip package manager, dimana hal itu berada di dalam _Virtual Environment_. Seperti perintah python, perintah `pip --version` pada sesi command prompt maka akan muncul versi dari `pip` tersebut yang aktif pada sesi _Virtual Environment_ saat ini.

## Install Python 3 Packages Dengan Pip

Untuk memasang Flask ke virtual environment pastikan _Virtual Environment_ `env` sudah aktif pada sesi saat ini, jika sudah maka jalankan perintah :

```text
(env) $ pip install flask
```

Ketika kamu menjalankan perintah ini, pip tidak hanya memasang Flask tapi juga semua dependensi yang dibutuhkan oleh Flask. Kamu dapat melakukan pengecekan packages apa saja yang saat ini terpasang di _Virtual Environment_ menggunakan perintah `pip freeze`

```text
(env) $ pip freeze       
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
pkg-resources==0.0.0
Werkzeug==0.16.0
```

Luaran dari perintah `pip freeze` berupa nama packages serta detail versi-nya. Kamu dapat memastikan apakah Flask sudah terpasang dengan memulai sesi Python Interpreter dan lakukan import seperti berikut :

```text
(env) $ python           
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
>>> 
```

Jika tidak muncul pesan error, itu tandanya kamu sudah siap untuk ke halaman berikutnya, dimana kita akan membuat sebuah aplikasi web!

