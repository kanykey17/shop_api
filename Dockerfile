FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install django djangorestframework psycopg2-binary python-dotenv djangorestframework-simplejwt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]