FROM python:3
WORKDIR /user/src/app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip,from=pip_cache pip install -r /app/requirements.txt

COPY main.py /user/src/app/
VOLUME /user/src/app

RUN apt-get -q update
RUN apt install netcat-traditional -y
RUN apt -y install iputils-ping

EXPOSE 8080

COPY wait-for .
CMD ["uvicorn","main:app","--reload"]
