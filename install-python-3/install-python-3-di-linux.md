# Install Python 3 di Linux

Pada umumnya, Python sudah terpasang pada Linux/Unix namun bukan versi Python yang terbaru. Pada panduan kali ini Python yang akan digunakan adalah versi 3.6, untuk memastikan versi Python yang telah terpasang dikomputer kita, lakukan pengecekan terlebih dahulu pada terminal dengan perintah :

```bash
$ python3 --version
Python 3.6.9
```

Jika versi yang muncul adalah `Python 2.7.x` maka sebaiknya kamu memasang Python versi 3.6 berdasarkan distribusi/distro Linux kamu.

**Ubuntu** 

Berdasarkan versi Ubuntu yang kamu punya, ada berbagai macam cara pemasangan Python. Sebelumnya kamu dapat melakukan pengecekan versi Ubuntu kamu dengan perintah

```bash
$ lsb_release -a
No LSB modules are available.
Distributor ID:     Ubuntu
Description:     Ubuntu 18.04.4 LTS
Release:         18.04
Codename:        bionic
```

Berdasarkan versi Rilis-nya, kamu dapat mengikuti perintah di bawah ini :

* **Ubuntu 17.10, Ubuntu 18.04** \(dan seterusnya\) sudah terpasang secara default Python 3.6 sehingga kamu sudah dapat menjalankan Python dengan perintah Python3
* **Ubuntu 16.10, Ubuntu 17.04** belum terpasang Python 3.6 namun tersedia di repository apt sehingga kamu harus memasang nya dengan cara :

```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```

* **Ubuntu 14.04, Ubuntu 16.04** tidak tersedia secara default di repository apt, sehingga kamu harus menambahkan Personal Package Archive \(PPA\). Sebagai contoh untuk memasang Python dari “deadsnakes” PPA dengan cara :

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
```

jika kamu menggunakan versi Linux lain nya, dapat melihat caranya disini : [https://realpython.com/installing-python/ ](https://realpython.com/installing-python/%20)

