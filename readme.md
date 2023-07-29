## Django Project Setup 

### 1. create virtual environment
```
virtualenv venv
```

### 2. activate virtual environment
```
source venv/bin/activate
```

### 3. install dependencies
```
pip install -r requirement.txt
```

### 4. create database
```
mysql -u root -p
```
```
CREATE DATABASE ssbm_db;
USE ssbm_db;
```
```
source mysql_dependency.sql
```

### 5. run migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 6. create superuser
```
python manage.py createsuperuser
```

### 7. run server
```
python manage.py runserver
```

