1. Django 설치

``` shell
pip install django
```

2. django-rest-framework 설치

``` shell
pip install djangorestframework
```

3. django-cors-header 설치

``` shell
pip install django-cors-headers
```

4. requests 라이브러리 설치

``` shell
pip install requests
```

5. SQLite3 설치

``` shell
apt-get install sqlite3
```

6. 프로젝트 생성

``` shell
django-admin startproject career_bot
```

7. app 생성

``` shell
cd career_bot
python manage.py startapp server
```

8. settings.py의 INSTALLED_APPS에 corsheaders, restframework, app 추가

``` python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'server',
]
```

9. settings.py의 MIDDLEWARE에 cors 관련 설정 추가

``` python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```

10. settings.py에 쿠키, http 메서드, url 관련 설정 추가

``` python
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PATCH',
    'PUT',
    'DELETE',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

11. 마이그레이션 수행

``` shell
python manage.py migrate
```

- 마이그레이션 오류 발생 시

``` shell
python manage.py makemigrations
python manage.py migrate
```

12. 프로젝트 시작

``` shell
python manage.py runserver
```