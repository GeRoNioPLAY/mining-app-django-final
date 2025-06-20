# Установка

- Клонирование репозитория

```sh
git clone https://github.com/GeRoNioPLAY/mining-app-django-final.git
cd .\mining-app-django-final\
```

- Создать виртуальное окружение

```sh
python.exe -m venv .venv
```

- Активировать виртуальное окружение

```sh
.\.venv\Scripts\activate
```

- Установка пакетов

```sh
pip install -r requirements.txt
```

- Настройка окружения
В файле `mining_app\mining_app\settings.py` настроить DATABASES.
Если нужно, есть файл mining_app_django.sql.

- Перейти в папку с проектом

```sh
cd .\mining_app\
```

- Если нужно, можно создать superuser (админа):

```sh
python.exe .\manage.py createsuperuser
```

- Применение миграций

```sh
python.exe .\manage.py makemigrations
python.exe .\manage.py migrate
```

# Запуск

```sh
python.exe .\manage.py runserver
```
