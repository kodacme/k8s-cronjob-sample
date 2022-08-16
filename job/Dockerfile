FROM python:3.9.2-alpine
COPY job.py /job.py
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "job.py"]
