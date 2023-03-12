FROM python:3.11.2-bullseye

# RUN

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN  pip install gunicorn

COPY . .

RUN mkdir -p '../logs'
RUN touch '../logs/exception.log'
RUN chmod -R 777 '../logs/exception.log'

CMD ["gunicorn","main.wsgi","--bind","0.0.0.0:8000"]
