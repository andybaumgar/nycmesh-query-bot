## Setup
- Open a terminal in the root repo directory.
- Ensure you have [Python](https://www.python.org/downloads/) with pip installed.
- `pip install -r requirements.txt`
- `pip install -e .`

This will install the package in "developer mode".  Subsequent changes to the files will automatically be reloaded.

## Running
- Open a terminal
- `python querybot`


### Running with Docker
- install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- start Docker Desktop
- clone the repo and open a shell in the root folder
- ensure you have a .env file with all required credentials
- run the following commands:
```shell
docker build . -t nycmesh-querybot
docker run --name nycmesh-querybot --rm -v "$PWD/.env:/app/.env" nycmesh-querybot
```

## CI
- To run multiple runners on the same server (necessary to execute code from different repositories) simply change the folder used for the runner ex. `actions-runner-nycmesh-querybot`
- To run a GitHub runner as a service, follow the instructions here: https://docs.github.com/en/actions/hosting-your-own-runners/configuring-the-self-hosted-runner-application-as-a-service