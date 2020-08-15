# Install Python 3 di MacOs

Sama seperti Linux, versi macOs sudah secara default ter-instal python namun python versi 2, sedangkan pada panduan ini Python yang digunakan adalah 3.8.1 maka kita akan melakukan upgrade pada python tersebut.

Cara terbaik yang dapat kita lakukan untuk melakukan instalasi Python 3 pada macOs adalah menggunakan [Homebrew Package Manager](https://brew.sh/).

**Langkah 1: Install Homebrew \(Part 1\)**

Sebelum memulainya, kamu diminta untuk install Homebrew:

* Buka terminal pada macOs Terminal Prompt, lalu paste command berikut ini dan tekan enter:

```text
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* Jika kamu melakukan hal ini di macOs yang masih baru, mungkin kamu akan mendapat pop up alert yang menanyakan apakah ingin menginstal Apple command line developer tools lalu konfirmasi dialog dengan klik install

Pada point ini, tunggu proses unduh command line developer tools hingga selesai di instal.

**Langkah 2: Install Python**

Ketika Homebrew berhasil di instal, kembali lagi ke terminal dan jalankan perintah:

```text
$ brew install python3
```

Ini akan mengunduh dan install versi Python terbaru. Setelah selesai, Python 3 sudah terpasang di macOs anda. Kamu dapat memastikan apakah Python 3 sudah terpasang, dengan cara:

```text
$ python3
Python 3.8.1
```

