FROM python:3.9-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY server.py /app
EXPOSE 5000
ENV FLASK_APP=server.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]