FROM python:3.10
#ADD DockerDemo.py .
RUN pip install requests atlassian-python-api
CMD ["python"]

