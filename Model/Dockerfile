FROM python:3

# 파이썬 버퍼 제거
ENV PYTHONUNBUFFERED=1
# 한글 인식
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

# 작업 파일 설정
# mkdir: cannot create directory '/project': File exists 오류가 나므로 주석처리? 다른곳은 정상인데 해방 부분에서 오류가 나는이 이해가 잘 안됨
#RUN mkdir /project
WORKDIR /project

# 파이썬 라이브러리 설치
COPY requirements.txt /project
RUN pip install -r requirements.txt

# -u 옵션으로 버퍼없이 즉시 출력
ENTRYPOINT ["python", "-u", "./main.py"]
