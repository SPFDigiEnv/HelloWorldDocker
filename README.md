# Hello World Docker
Test app to showcase Docker bind mounts at [runtime](https://docs.docker.com/engine/reference/commandline/run/). <i>Issue addressed - how to edit source code files locally so a running Docker container image can execute them.</i>

## Background
[Docker](https://docs.docker.com/get-started/overview/) is an open platform for developing, shipping, and running applications. Docker enables separation of 'containerised' applications from local computing infrastructure.

Using docker means not having to have applications installed locally, instead running them in 'sealed' containers, held discrete from the local computer. In a Use Case of developing code in Python for example, a docker container holding the latest version of Python, plus the Python script can be built and run.

However, in this case, to edit the Python script and rerun it, the image container needs to be rebuilt each time there are edits made to the code. Docker has the ability to use 'bind mounts' to circumvent this for development purposes. The folder holding the source code is 'mounted' into the container image, meaning that the code can then be edited and run immediately in the image without needing to be rebuilt each time.

To run these examples, and assuming docker is installed on the local computer, download this repo and run the docker commands below from the command line when in this local folder. If Docker has not been used before, the initial build may take a while as the latest Python image is downloaded for the first time. First, run the code 'without bind mounting' (the files in the repo), next edit the docker file as noted and rerun 'with bind mounting'. Try editing the local Python source code each time, perhaps changing the message it prints, to see the difference.  

## Developing without bind mounting
In the first approach, the code is implemented without bind mounting. Here the source code is <i>copied</i> into the container, and can then be run from there. However, to edit the local source code to make any changes, the container will have to be rebuilt again after each time edits are made. The workflow is (1) edit the file and then (2) rebuild and (3) run the Python script in the container CLI as below. Note one can still edit the code copied into the container - but it is then out of sync with the local copy.

### The Dockerfile
The Dockerfile (as in git) will be:<br />
`FROM` = Use the image with the latest version of Python<br />
`WORKDIR` = create a working folder in the image '/app'<br />
`COPY` = copy the Python 'py' script files from the current folder into the working folder in the image.

```
FROM python:latest
WORKDIR /app
COPY *.py ./
```

### Build container
To construct the docker file:<br />
`-t` = use nametag (here 'hello-world-docker')<br />
`.` = with files in current folder

```
docker build -t hello-world-docker .
```

### Run container
To run the docker file:<br />
`-d` = background<br />
`-i` = interactive

```
docker run -di hello-world-docker
```

## Running the code
To run the source code file from within the container at the CLI (command line interface). Note the source code cannot be edited - but the original script version can be run as below:<br />

```
python hello_world_docker.py
```

## Developing with bind mounting
In the second approach, the code is implemented 'with docker bind mounting'. This is achieved with flags set in the `docker run` command. Here the source code is held locally, but <i>referenced</i> within the container, and can be run. To edit the code to make any changes, the container will reference the edited file immediately as the edits are made. The image does not need to be rebuilt first. The workflow is (1) update the docker file and rebuild the image, (2) then in the container CLI run the python script, (3) edit the local Python script and rerun in the container to see the result.

### The Dockerfile
The Dockerfile will be edited (commenting or removing the other lines) to:

```
FROM python:latest
```

### Build container
To construct the docker file:<br />
`-t` = use nametag (here 'hello-world-docker')<br />
`.` = with all the files in current folder

```
docker build -t hello-world-docker .
```

### Run container
To run the docker file, to bind mount the development code instead of copying it:<br />
`-d` = background<br />
`-i` = interactive<br />
`-v` = (from):(to)     - $(pwd) means the 'current folder'<br />
`-w` = working folder

```
docker run -di -v $(pwd):/app -w /app hello-world-docker
```

## Running the code
To run the source code file from within the container at the CLI (command line interface). The source code can be edited locally and then just re-run in the container as below:

```
python hello_world_docker.py
```

## Epilogue - using Docker Compose
Docker compose helps simplify the process of running models (quite a simple one in this case - but still), see [Use Docker Compose](https://docs.docker.com/compose/reference/) and [Overview of Docker-Compose CLI](https://docs.docker.com/compose/reference/). To use docker-compose, you create a yaml model definition file, named `docker-compose.yml` with all the settings needed to run the model.

In this case, we wish to use a yml file to recreate the run command:

```
docker run -di -v $(pwd):/app -w /app hello-world-docker
```

The docker-compose.yml file will contain the following:

```
version: "3.7"
services:
  app:
    stdin_open: true # equivalent to docker run -i
    tty: true        # equivalent to docker run -t
    image: hello-world-docker
    working_dir: /app
    volumes:
      - ./:/app
```

The docker-compose command can then be run from the project folder with the command `docker-compose up`, and stopped with `docker-compose down`. This approach is considered good practice because, as models get more complex, so that complexity can be managed via the yml file - simplifying the running of the code. In Docker desktop, the CLI command is nested in the App hierarchy.
