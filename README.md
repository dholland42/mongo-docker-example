# MongoDB Example for NIH Reporter API

This is a small example of connecting a python application that pulls data from the
[NIH Reporter API](https://api.reporter.nih.gov) and stores it in a MongoDB collection.


To play around with this example, you will need to install docker and docker-compose
(if you install docker via docker desktop, you will already have docker-compose).

## Run the Example

The [`build.sh`](./build.sh) script will build both of the docker images needed. The
definitions of those containers live in [`mongo/Dockerfile`](./mongo/Dockerfile) and
[`app/Dockerfile`](./app/Dockerfile). You can update and configure the images from those
files as needed.

Then you can run `docker compose up` to start both containers. The `app` container will
start a jupyter notebook server. You should see the necessary url in the command output
to access the notebook server.

```sh 
$ sh build.sh
...
$ docker compose up
...
app-1    | [I 2025-03-27 19:53:54.065 ServerApp] Jupyter Server 2.15.0 is running at:
app-1    | [I 2025-03-27 19:53:54.065 ServerApp] http://<container-id>:80/tree?token=<token>
app-1    | [I 2025-03-27 19:53:54.065 ServerApp]     http://127.0.0.1:80/tree?token=<token>
...
```
