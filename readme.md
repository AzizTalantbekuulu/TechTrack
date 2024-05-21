# TechTrach Project

## Описание проекта
Проект "Технический мониторинг" представляет собой систему управления техническими данными и оборудованием. Он предоставляет API для регистрации пользователей, управления оборудованием и записи данных о его состоянии.

## Используемые технологии
- Python
- Django
- Django REST Framework
- Django REST Framework SimpleJWT
- PostgreSQL

## Установка
1. Клонируйте репозиторий:
```bash
   git clone https://github.com/AzizTalantbekuulu/TechTrack.git
```
2. Установите зависимости:
```bash
   pip install -r requirements.txt
```
3. Создайте базу данных PostgreSQL и настройте соединение в файле settings.py.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TechTrack',
        'USER': 'Your_username',
        'PASSWORD': 'Your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
4. Выполните миграции:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустите сервер:
```bash
python manage.py runserver
```
## Использование

### Аутентификация
Для доступа к защищенным эндпоинтам необходимо получить токен аутентификации, используя эндпоинт `/api/token/`.

### Эндпоинты API

- **Регистрация нового пользователя:** `POST /api/register/`
- **Логин пользователя:** `POST /api/token/`
- **Получение нового доступного токена:** `POST /api/token/refresh/`
- **Пользователи:**
  - `GET /api/users/`
  - `POST /api/users/`
  - `GET /api/users/<user_id>/`
  - `PUT /api/users/<user_id>/`
  - `PATCH /api/users/<user_id>/`
  - `DELETE /api/users/<user_id>/`
- **Оборудование:**
  - `GET /api/equipment/`
  - `POST /api/equipment/`
  - `GET /api/equipment/<equipment_id>/`
  - `PUT /api/equipment/<equipment_id>/`
  - `PATCH /api/equipment/<equipment_id>/`
  - `DELETE /api/equipment/<equipment_id>/`
- **Данные для оборудования:**
  - `GET /api/equipment/<equipment_id>/data/`
  - `POST /api/equipment/<equipment_id>/data/`
  - `GET /api/equipment/<equipment_id>/data/<data_id>/`
  - `PUT /api/equipment/<equipment_id>/data/<data_id>/`
  - `PATCH /api/equipment/<equipment_id>/data/<data_id>/`
  - `DELETE /api/equipment/<equipment_id>/data/<data_id>/`

Каждый эндпоинт требует аутентификации через токен. Для этого в заголовках запроса необходимо указать `Authorization: Bearer <access_token>`.

## Images

#### Swagger
![image](https://github.com/AzizTalantbekuulu/TechTrack/assets/97390701/02830b7f-f448-4b8c-be39-e09f6efc2237), ![image](https://github.com/AzizTalantbekuulu/TechTrack/assets/97390701/ce94beea-334a-4f49-9359-7069c6f69821)
### Redoc
![image](https://github.com/AzizTalantbekuulu/TechTrack/assets/97390701/4e86c86f-0d50-4096-ad90-68303b331509), ![image](https://github.com/AzizTalantbekuulu/TechTrack/assets/97390701/e2b6f601-c311-46a9-9180-35c6f7840cc2)

### Документация API
Полная документация API доступна по следующим ссылкам:
- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [Redoc](http://127.0.0.1:8000/redoc/)
Подробнее о каждом эндпоинте и допустимых операциях смотрите в документации API.

## Github
https://github.com/AzizTalantbekuulu/TechTrack
