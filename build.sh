#! /usr/bin/env sh

docker build -t mongodb -f mongo/Dockerfile mongo/
docker build -t app -f app/Dockerfile app/
