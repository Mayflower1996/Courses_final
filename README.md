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

    docker build -t myjenkins .


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

Repo admin: 
jjgraffity@gmail.com

<h1 align="center">Hi, I'm Ivan Ogurtsov</h1>
<h3 align="center">A passionate AQA from Belarus</h3>

- All of my projects are available at [https://github.com/Mayflower1996](https://github.com/Mayflower1996)

- How to reach me **minsk.ivan.ogurtsov@gmail.com**

- Know about my experiences [https://www.linkedin.com/in/ivan-ogurtsov-aqa/](https://www.linkedin.com/in/ivan-ogurtsov-aqa/)

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/ivan ogurtsov" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="ivan ogurtsov" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.elastic.co" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/elastic/elastic-icon.svg" alt="elasticsearch" width="40" height="40"/> </a> <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://grafana.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/grafana/grafana-icon.svg" alt="grafana" width="40" height="40"/> </a> <a href="https://www.jenkins.io" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/jenkins/jenkins-icon.svg" alt="jenkins" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.microsoft.com/en-us/sql-server" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="mssql" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>



