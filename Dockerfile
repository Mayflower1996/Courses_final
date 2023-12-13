FROM python:3.12

RUN pip install --upgrade pip

WORKDIR /usr/src/the-pyoneers

COPY req.txt .
RUN pip install -r req.txt

COPY . .

EXPOSE 80

CMD ["pytest", "tests/"]