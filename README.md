### Server

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
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/kosts.proto
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

### Client

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
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/kosts.proto
```

6. Jalankan gRPC Client

```
pserve development.ini --reload
```
