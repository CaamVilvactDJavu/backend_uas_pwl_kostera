# UAS PEMROGRAMAN WEB LANJUT

## Pengembangan Aplikasi Web Kostera menggunakan Metode _Modified Iterative Waterfall_

## Anggota Kelompok

**Fachri Ahmad - 120140124**\
**Ilham Fadhlur Rahman - 120140125**\
**Duta Rega Rolindo Simorangkir - 120140135**\
**Rizqi Fiesta Febrianto - 1201401171**

## Daftar isi

1. [Server](#server)
   1. [Cara Menjalankan Server Side](#cara-menjalankan-server-side)
   2. [Library Server Side](#library-server-side)
2. [Client](#client)
   1. [Cara Menjalankan Client Side](#cara-menjalankan-client-side)
   2. [Library Client Side](#library-client-side)
3. [API Routes](#api-routes)
   1. [Endpoints Kost](#endpoints-kost)
   2. [Endpoints Autentikasi](#endpoints-autentikasi)

### Server

#### Cara Menjalankan Server Side

1. Ganti ke Directory Server

```
cd server
```

2. Install Virtual Environment

```
python3 -m venv env
```

3. Aktifkan Virtual Environment

```
env\Scripts\activate
```

4. Install Dependencies dan Update pip

```
python -m pip install --upgrade pip setuptools
```

```
pip install -e .
```

5. Generate gRPC

```
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/kosts.proto ../protos/auth.proto
```

6. Buat Database

```
Buat database (mysql) dengan nama backend_uas_pwl_kostera
```

7. Migrate Database

```
alembic upgrade head
```

8. Jalankan gRPC Server

```
python -m server
```

#### Library Server Side

| Library                | Fungsi                                                                                                                                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alembic                | **alembic** adalah sebuah tool yang digunakan untuk manajemen versi skema database dalam proyek Pyramid. Fungsi utama **alembic** melibatkan migrasi database, yang melibatkan perubahan struktur atau skema database.                      |
| SQLAlchemy             | **SQLAlchemy** adalah library Python yang umum digunakan untuk berinteraksi dengan database.                                                                                                                                                |
| grpcio                 | **grpcio** adalah library Python yang digunakan untuk mengimplementasikan gRPC (gRPC Remote Procedure Calls).                                                                                                                               |
| grpcio-tools           | **grpcio-tools** menyediakan alat perintah baris untuk menghasilkan kode Python dan definisi stub dari file Protobuf.                                                                                                                       |
| PyMySQL                | **PyMySQL** adalah library yang digunakan untuk melakukan operasi database pada MySQL.                                                                                                                                                      |
| mysql-connector-python | **mysql-connector-python** adalah library Python yang menyediakan konektor MySQL.                                                                                                                                                           |
| pyramid_jwt            | **pyramid_jwt** menyediakan dukungan untuk otentikasi berbasis JWT. Dalam project ini, **pyramid_jwt** digunakan untuk menangani aspek otentikasi dan otorisasi yang berkaitan dengan token JWT.                                            |
| PyJWT                  | **PyJWT** adalah library yang digunakan untuk mengamankan pertukaran informasi antar pihak. Dalam project ini, **PyJWT** digunakan untuk membuat token JWT yang berisi informasi pengguna dan peran (roles) setelah pendaftaran atau login. |
| bcrypt                 | Library **bcrypt** digunakan untuk menghasilkan hash password yang aman. Dalam project ini, **bcrypt** digunakan untuk melakukan hashing password pada saat registrasi dan verifikasi login.                                                |

### Client

#### Cara Menjalankan Client Side

1. Ganti ke Directory Client

```
cd client
```

2. Install Virtual Environment

```
python3 -m venv env
```

3. Aktifkan Virtual Environment

```
env\Scripts\activate
```

4. Install Dependencies dan Update pip

```
python -m pip install --upgrade pip setuptools
```

```
pip install -e .
```

5. Generate gRPC

```
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/kosts.proto ../protos/auth.proto
```

6. Jalankan gRPC Client

```
pserve development.ini --reload

```

#### Library Client Side

| Library      | Fungsi                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| grpcio       | **grpcio** adalah library Python yang digunakan untuk mengimplementasikan gRPC (gRPC Remote Procedure Calls).                                                                                    |
| grpcio-tools | **grpcio-tools** menyediakan alat perintah baris untuk menghasilkan kode Python dan definisi stub dari file Protobuf.                                                                            |
| pyramid_jwt  | **pyramid_jwt** menyediakan dukungan untuk otentikasi berbasis JWT. Dalam project ini, **pyramid_jwt** digunakan untuk menangani aspek otentikasi dan otorisasi yang berkaitan dengan token JWT. |

### API Routes

#### Endpoints Kost

| Method | Route             | Deskripsi                                                                                                    |
| ------ | ----------------- | ------------------------------------------------------------------------------------------------------------ |
| GET    | /kost             | Mendapatkan daftar semua kost.                                                                               |
| GET    | /kost?kostId={id} | Mendapatkan detail kost berdasarkan **kostId**.                                                              |
| POST   | /kost             | Membuat kost baru. Membutuhkan **name** dalam body request; attribute lainnya bersifat opsional.             |
| PUT    | /kost             | Memperbarui kost yang sudah ada. Membutuhkan **id** dalam body request; attribute lainnya bersifat opsional. |
| DELETE | /kost             | Menghapus kost yang sudah ada. Membutuhkan **id** dalam body request.                                        |

#### Endpoints Autentikasi

| Method | Route             | Deskripsi                                                                                                          |
| ------ | ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| POST   | /auth/register    | Mendaftarkan pengguna baru. Membutuhkan **username**, **password**, dan opsional **role** (default adalah "user"). |
| POST   | /auth/admin_login | Login admin. Membutuhkan **username** dan **password**.                                                            |
| POST   | /auth/login       | Login pengguna. Membutuhkan **username** dan **password**.                                                         |
| POST   | /auth/verify      | Memverifikasi **token** pengguna. Membutuhkan **token**.                                                           |
