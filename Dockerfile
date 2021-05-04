FROM python:3.7

COPY manage.py gunicorn-cfg.py requirements.txt .env ./
COPY app app
COPY authentication authentication
COPY core core
COPY weights weights
COPY staticfiles staticfiles

RUN apt-get install python-software-properties -y
RUN apt-add-repository ppa:nginx/stable
RUN apt-get update
RUN apt-get install nginx
COPY nginx.conf /etc/nginx/sites-enable/default.org
RUN /etc/init.d/nginx restart

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 5005
EXPOSE 8000
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
