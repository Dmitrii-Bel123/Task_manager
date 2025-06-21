# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем зависимости PostgreSQL для psycopg2
# Устанавливаем другие необходимые пакеты, включая git для возможной установки пакетов из репозиториев
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev git \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . /app/

# Открываем порт, на котором будет работать Django
EXPOSE 8000

# Команда, которая будет выполняться при запуске контейнера
# (Мы будем использовать Gunicorn в продакшене, но для разработки Django-сервер подойдет)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Закомментируем CMD пока, так как Docker Compose будет управлять запуском.