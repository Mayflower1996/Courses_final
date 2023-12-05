# Pet Store API Testing with Pytest Framework #

This repository contains automated API tests for the Pet Store, covering the `/user`, `/pet`, and `/store` endpoints, using the Pytest framework. 
These tests help ensure the functionality and reliability of the Pet Store API.

## Prerequisites

Before running the tests, make sure you have the following prerequisites installed:

- Python 3.x: https://www.python.org/downloads/
- Pip: https://pip.pypa.io/en/stable/installation/
- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Installation

1. Clone the repository:

git clone https://yourusername/course-auto/the-pyoneers.git
pip install -r req.txt


*** Configuration ***
base_url: http://petstore.swagger.io/v2

## Running the Tests
User endpoint: pytest Tests/user_tests_and_data
Pet endpoint: pytest Tests/pet_tests_and_data
Store endpoint: pytest Tests/store_tests_and_data


# Running All Tests
To run all the tests, execute the following command:
pytest

## Test Structure
The tests are organized in the Tests directory. Each endpoint (e.g., /user, /pet, /store) has its own test folder and files.

## Generating Reports
Pytest Framework will generate test reports in HTML format.

## Test Results
After running the tests, you can find the test results in the output directory. Open the HTML report in your web browser to view the test results.

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes. Make sure your code passes the CircleCI. Leave PR for review for other team member.

# Issues and Bug Reports
If you encounter any issues or find bugs in the tests, please report them to Google Excel (request from the team)

Make sure to replace `yourusername` and any other placeholders with your actual information. This README provides a clear guide on how to set up, configure, 
and run the tests using the ROBOT framework for the Pet Store API.

## Who do I talk to?

Repo admins: 
yuliya.bychyk@gmail.com
minsk.ivan.ogurtsov@gmail.com
tanittoki@gmail.com
