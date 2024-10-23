# Сравнение REST API на Django Rest Framework, FastAPI и Flask-RESTful

## Описание проекта
Этот проект направлен на сравнение трех различных фреймворков для разработки REST API: **Django Rest Framework**, **FastAPI** и **Flask-RESTful**. Цель проекта — продемонстрировать различия в подходах, производительности и удобстве разработки между этими инструментами.

## Структура проекта
Проект состоит из трех отдельных приложений:
- `drf_app`: приложение на **Django Rest Framework**.
- `fastapi_app`: приложение на **FastAPI**.
- `flask_app`: приложение на **Flask-RESTful**.

Каждое приложение предоставляет API для работы с данными пользователей, используя общий набор CRUD операций.

Django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/items/
http://127.0.0.1:8000/api/items/

Fastapi
uvicorn main:app --reload
http://127.0.0.1:8000
http://127.0.0.1:8000/items/
http://127.0.0.1:8000/items/1
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

GET /items/
GET /items/{item_id} 

### Файловая структура
 

project_root/
│   README.md
│   requirements.txt
│
├───drf_app/
│   ├───detection_site
│   │   ├───asgi.py
│   │   ├───settings.py
│   │   ├───urls.py
│   │   ├───wsgi.py
│   │   └───__init__.py
│   └───object_detection
│       ├───admin.py
│       ├───apps.py
│       ├───models.py
│       └───views.py
│
├───fastapi_app/
│   ├───main.py
│   ├───models.py
│   └───views.py
│
├───flask_app/
│   ├───app.py
│   ├───models.py
│   └───views.py
└───media/
    └───images/


## Установка и запуск

### Шаг 1: Клонировать репозиторий
```bash
git clone https://github.com/yourusername/rest-api-comparison.git
cd rest-api-comparison

### Шаг 2: Установка зависимостей
Перед установкой зависимостей убедитесь, что у вас установлен Python 3.11+ и виртуальное окружение.

1. Установка зависимостей для всех фреймворков:

```bash```

pip install -r requirements.txt

2. Запуск приложений:
Фреймворк Django Rest:

bash

cd drf_app
python manage.py migrate
python manage.py runserver
FastAPI:

```bash```

cd fastapi_app
uvicorn main:app --reload
Flask-Успокаивающий:

```bash```


cd flask_app
python app.py

Шаг 3: Доступ к API
Джанго: http://127.0.0.1:8000/
FastAPI: http://127.0.0.1:8000/docs (Swagger документация)
Колба: http://127.0.0.1:5000/
Тестирование
Каждое приложение поддерживает стандартные CRUD операции для работы с пользователями.

Примеры запросов:
Получение всех пользователей (GET):
Джанго: http://127.0.0.1:8000/api/users/
FastAPI: http://127.0.0.1:8000/users/
Колба: http://127.0.0.1:5000/users/
Добавление нового пользователя (POST):
json


{
  "username": "new_user",
  "age": 25
}
Сравнение
После выполнения тестов вы можете сравнить следующие параметры:

Скорость обработки запросов.
Простота написания кода.
Документация и поддержка фреймворка.

Заключение
Проект демонстрирует, что Django Rest Framework предлагает встроенные функции, FastAPI выигрывает в производительности, а Flask-RESTful обеспечивает гибкость и простоту, но требует больше кода для реализации базовых функций.```
