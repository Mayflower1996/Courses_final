# Pet Store API Testing with ROBOT Framework #

This repository contains automated API tests for the Pet Store, covering the `/user`, `/pet`, and `/store` endpoints, using the ROBOT framework. 
These tests help ensure the functionality and reliability of the Pet Store API.

## Prerequisites

Before running the tests, you need to have the following prerequisites installed on your system:

- Python 3.x
- ROBOT Framework
- Requests Library for ROBOT Framework

You can install ROBOT Framework and the Requests library using pip:

pip install robotframework
pip install robotframework-requests

## Configuration
Clone this repository to your local machine:

git clone https://yourusername/course-auto/the-pyoneers.git

Open the tests/variables.robot file and set the base URL for the Pet Store API if necessary:

*** Variables ***
${BASE URL}    http://petstore.swagger.io/v2

## Running the Tests
You can run the tests using the ROBOT framework command-line tool. Here are the basic commands for running the tests:

# Running All Tests
To run all the tests, execute the following command:

robot tests

# Running Specific Tests
You can also run specific test suites or individual test cases by specifying their paths:

robot tests/test_suite_name.robot

## Generating Reports
ROBOT Framework generates test reports in HTML format. To generate a report, use the --output option:

robot --output output.html tests

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
