FROM python:3.7

ENV DEBUG True

COPY manage.py gunicorn-cfg.py requirements.txt .env ./
COPY app app
COPY authentication authentication
COPY core core
COPY weights weights
COPY staticfiles staticfiles

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install nginx -y
COPY nginx.conf /etc/nginx/sites-enable/default.org
RUN /etc/init.d/nginx restart

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 5005 8000
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
