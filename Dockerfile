FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /Collect
WORKDIR /collect
COPY ./ ./
RUN pip install -r requirements.txt
ENV DEBUG=1
ENV ALLOWED_HOSTS=*
ENV REDIS='redis://redis:6379'
ENV SECRET_KEY=1v3&61&#p(g-x!c%zix&-5t-%efp&xc$m+qu*+7pzcwatzxfq0
#RUN python manage.py makemigrations --noinput
#RUN python manage.py migrate --noinput
CMD ["./script.sh"]