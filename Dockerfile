FROM python:3.7
ADD hello.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "hello.py"]