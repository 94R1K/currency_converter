# Конвертер валют для Айти Гуру

# Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-464646?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

# Kак запустить

### Клонируем проект:
```shell
git clone https://github.com/94R1K/currency_converter.git
```

### Открываем консоль в проекте и переходим в папку «infra»:
```shell
cd infra
```

### Запускаем docker-compose с помощью команды:
```shell
docker-compose up -d
```
или
### для macOS/Linux систем:
```shell
sudo docker-compose up -d
```

# Ура! Можно тестировать проект 🙌

### Конвертер валют доступен по адресу:
```link
http://localhost/api/rates?from=USD&to=RUB&value=1
```
или
```link
http://127.0.0.1:8000/api/rates?from=USD&to=RUB&value=1
```

# Об авторе
Лошкарев Ярослав Эдуардович \
Россия, г. Москва \
E-mail: yaluv.py@yandex.ru 

[![VK](https://img.shields.io/badge/Вконтакте-%232E87FB.svg?&style=for-the-badge&logo=vk&logoColor=white)](https://vk.com/yalluv)
[![TG](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/yallluv)
