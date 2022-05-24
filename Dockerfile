FROM python:3.10-buster

#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - 

RUN pip3 install poetry

RUN export PATH="$HOME/.poetry/bin:${PATH}"
WORKDIR /home/app

COPY . .

RUN poetry install

EXPOSE 5001/tcp

CMD ["poetry", "run", "python3", "flask_k8s_practice/coingecko_api.py"]