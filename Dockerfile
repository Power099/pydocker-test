FROM python:3
WORKDIR /user/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY py_mariadb.py /user/src/app/
VOLUME /user/src/app

RUN apt-get -q update
RUN apt install netcat-traditional -y
RUN apt -y install iputils-ping

EXPOSE 8080

COPY wait-for .

