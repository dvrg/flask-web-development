# Virtual Environment di Python

Sekarang kamu telah membuat direktori aplikasi, kemudian saatnya untuk menginstall Flask. Cara yang paling mudah adalah dengan menggunakan _Virtual Environment_. _Virtual Environment_ adalah salinan dari bahasa Python di mana kamu dapat menginstal paket secara private tanpa mempengaruhi paket Python secara global. 

Lingkungan virtual sangat berguna karena mencegah ketidaksesuaian dan konflik antar paket dalam interpreter Python sistem. _Virtual Environment_ berfungsi juga untuk menjaga sistem kamu tetap rapi dalam development.

## Membuat Virtual Environment Python 3

Selanjutnya kamu akan membuat _Virtual Environment_. Caranya pertama kamu harus install package standard untuk membuat environment, buka terminal \(Linux/Unix\) / command prompt \(Windows\) :

#### Linux/Unix

```text
$ python3 -m venv env
```

#### Windows

```text
$ py -m venv env
atau
$ python -m venv env
```

Jika terdapat masalah ketika membuat _Virtual Environtment_ pada Linux, terlebih dahulu install package `python3-venv` dengan cara :

```text
$ sudo apt-get install python3-venv
```

**Keterangan Perintah :**

| Script | Keterangan |
| :---: | :---: |
| python3 | Untuk menjalankan python |
| -m | Untuk menjalankan module |
| venv | virtual environtment |
| env | nama virtual environtment |

## Menggunakan Virtual Environment

Virtual environment kamu sudah terbuat, sekarang kamu tinggal mengaktifkan environment dengan menggunakan perintah ini dan pastikan kamu sudah tepat di direktori tempat install environmentnya :

**Linux \(Ubuntu/ Debian\) / Mac**

```text
$ env/bin/activate
atau
$ source env/bin/activate    
```

**Windows**

```text
$ env\Scripts\activate
```

maka terminal kamu akan berubah menjadi

```text
(env) $
```

Dan untuk deactivatenya cukup ketikkan perintah:

```text
(env) $ deactivate
```

