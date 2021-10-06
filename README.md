# Hello World Docker
# Test app to showcase Docker bind mounts

## Background
[Docker](https://docs.docker.com/get-started/overview/) is an open platform for developing, shipping, and running applications. Docker enables separation of 'containerised' applications from local infrastructure.

Using docker locally means not having to have applications installed locally, but instead running in 'sealed' containers, discrete from the local computer. In a Use Case of developing code in Python for example, a docker container holding the latest version of Python, plus the Python script can be built and run.

However, to edit the Python script and rerun it, the image container needs to be rebuilt each time there are changes made. Docker has the ability to use bind mounts to circumvent this for development. The folder with the source code is 'mounted' into the container image, meaning that the code can be edited and then run immediately in the image without needing to be rebuilt.

## Developing without bind mounting
In the first version, the code is implemented without bind mounting. Here the source code is <i>copied</i> into the container, and can be run. However, to edit the code to make any changes, the container will have to be rebuilt after each time edits are made.

### The Dockerfile
The Dockerfile will be:
FROM = Use the image with the latest version of Python
WORKDIR = create a working folder in the image '/app'
COPY = copy the Python 'py' script files from the current folder into the working folder in the image.

```
FROM python:latest
WORKDIR /app
COPY *.py ./
```

### Build container
To construct the docker file:
-t = use nametag (here 'hello-world-docker')
'.' = with files in current folder

```
docker build -t hello-world-docker .
```

### Run container
To run the docker file:
-i = interactive
-d = background

```
docker run -di hello-world-docker
```

## Running the code
The source code cannot be edited - but the original version can be run:

```
python hello_world_docker.py
```

## Developing with bind mounting
In the second version, the code is implemented with docker bind mounting. Here the source code is <i>referenced</i> within the container, and can be run. To edit the code to make any changes, the container will reference the edited file after the edits are made.

### The Dockerfile
The Dockerfile will be:

```
FROM python:latest
```

### Build container
To construct the docker file:
-t = use nametag (here 'hello-world-docker')
'.' = with all the files in current folder

```
docker build -t hello-world-docker .
```

### Run container
To run the docker file, to bind mount the development code instead of copying it:
-i = interactive
-d = background
-v = (from):(to)     - $(pwd) means the 'current folder'
-w = working folder

```
docker run -di -v $(pwd):/app -w /app hello-world-docker
```

## Running the code
The source code can be edited and then just re-run as above:

```
python hello_world_docker.py
```
