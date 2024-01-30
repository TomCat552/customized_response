FROM python:3.9-alpine

WORKDIR /home/customized_response


# 将当前目录文件复制到工作目录
# COPY . .


COPY requirements.txt . && COPY requirements.txt server.py ./ && COPY static ./static/

RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
CMD [ "python", "server.py" ]