FROM python:3.8.1-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python","api.py"]