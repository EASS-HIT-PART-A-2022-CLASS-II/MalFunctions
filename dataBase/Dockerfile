FROM python:3.9

RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install requests
RUN pip install mysql-connector-python
WORKDIR /app
COPY . .

EXPOSE 80

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
