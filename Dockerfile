FROM python:3-alpine
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && gunicorn main.wsgi:application --bind 0.0.0.0:8000"]
