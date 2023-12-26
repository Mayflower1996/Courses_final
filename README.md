# Pet Store API Tests

This repository contains automated tests for the Pet Store API. The tests cover
the `/user`, `/pet`, and `/store` endpoints using the pytest framework. Additionally,
Docker is used to facilitate testing and running builds within a 'myjenkins' container.

## Prerequisites

- Docker installed on your machine
- Docker images 'myjenkins' and 'swaggerapi/petstore' available
- Jenkins installed on Docker Desktop
- Bitbucket account and repository
- Allure command-line tool installed

## Running Tests Locally

1. Clone this repository to your local machine:

    git clone https://yourusername/course-auto/the-pyoneers.git
    cd tests

2. Install dependencies:

    pip install -r req.txt

3. Run the tests using pytest:

    pytest

    This will execute all tests in the repository. You can specify a specific test file or directory if needed.
    E.g. pytest store-tests

## Test Structure

The tests are organized in the 'tests' directory. Each endpoint (e.g., /user, /pet, /store) has its
own test folder and files. Data for running tests are stored in 'data_for_tests' directory.

## Running Tests in Docker

1. Build the Docker image:

    docker build -t myjenkins


## Setting up Jenkins on Docker Desktop

1. Open Docker Desktop and click on "Ports."

2. Access Jenkins in your browser at `http://localhost:8080`.

3. Follow the Jenkins setup wizard to complete the installation.

4. Install necessary Jenkins plugins, including the Bitbucket plugin.


## Configuring Jenkins Job

1. Request team to provide Pipeline script 


## Reports

Allure reports are configured in Jenkins. Reports are available after finished job in Jenkins.

Now, Jenkins will pull the 'myjenkins' Docker image, clone the repository, and run the tests in a Docker container.

Make sure to replace `yourusername` and any other placeholders with your actual information. 

## Who do I talk to?

Repo admins: 
yuliya.bychyk@gmail.com
minsk.ivan.ogurtsov@gmail.com
tanittoki@gmail.com

