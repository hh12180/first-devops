FROM python:3.10-slim
WORKDIR /my_website
RUN pip install flask
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
