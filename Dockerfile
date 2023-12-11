FROM python:3.9
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY . .
CMD ["pytest", "tests", "--alluredir", "allure-results"]