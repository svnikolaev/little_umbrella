FROM python:3.10.2-slim

ARG userid=1000
ARG groupid=1000
RUN groupadd -g $groupid user && useradd -u $userid -g user user
VOLUME [ "/usr/src/app" ]
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER user
CMD ["python3"]