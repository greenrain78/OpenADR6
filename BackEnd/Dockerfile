FROM python:3.7

# 파이썬 버퍼 제거
ENV PYTHONUNBUFFERED=1

# 작업 파일 설정
RUN mkdir /project
WORKDIR /project

# 파이썬 라이브러리 설치
COPY . /project
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "/project/entrypoint.sh"]

# -u 옵션으로 버퍼없이 즉시 출력
CMD ["python", "manage.py", "runserver", "0:8000"]
