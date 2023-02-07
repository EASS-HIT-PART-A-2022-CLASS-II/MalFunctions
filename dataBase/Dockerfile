FROM python:3.9
COPY ./req.txt .
RUN pip install -r req.txt


WORKDIR /app
COPY . .

EXPOSE 80

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
