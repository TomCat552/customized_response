FROM python:3.9-alpine

WORKDIR /home/customized_response

# COPY requirements.txt .
# 将当前目录文件复制到工作目录

COPY . .

RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
CMD [ "python", "server.py" ]