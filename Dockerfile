# Используем официальный образ Python в качестве базового
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt в рабочую директорию
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . .

# Устанавливаем переменную окружения для указания Flask, что мы в режиме разработки
ENV FLASK_ENV=development

# Указываем порт, который будет использован
EXPOSE 5001

# Команда для запуска приложения
CMD ["python", "run.py"]
