FROM python:3
WORKDIR /user/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY main.py /user/src/app/
VOLUME /user/src/app

EXPOSE 8080

CMD ["uvicorn","main:app","--reload"]
