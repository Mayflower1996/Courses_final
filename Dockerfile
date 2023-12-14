FROM jenkins/jenkins:2.426.2-lts-jdk17

USER root

RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
