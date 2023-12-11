FROM python:3.11
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY . .
CMD ["pytest", "tests", "--alluredir", "allure-results"]