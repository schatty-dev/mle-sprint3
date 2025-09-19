FROM python:3.11-slim
# возьмём образ, который мы скачали ранее и в котором уже установлен Python

LABEL author="mle-student"

COPY . ./my_super_dir

WORKDIR my_super_dir 
# изменяем рабочую директорию Docker 
# эта команда похожа на инструкцию RUN ["cd", "./my_super_dir"]
# в документации Docker рекомендуется использовать именно WORKDIR

CMD ["python3", "./main.py"]
# эта инструкция указывает ту команду, которая должна выполниться при старте контейнера