# Handy Bot

## Purpose

Making the lives of handymen easier by leveraging GenAI to improve client interactions

## Setup

### Get GCP Setup

1. Install the `gcloud cli` on your local machine. Follow this [page](https://cloud.google.com/sdk/docs/install)

2. Clone the handy bot github repository through `git clone https://github.com/Austinmc41/handy-dynamics.git`

3. Navigate to `handy-dynamics/` directory in your machine

4. Run `gcloud init` (in the interactive prompt, provide your google cloud email that's granted access to `handy-bot` project)

5. Run `gcloud auth application-default login`

6. Setup Google Cloud SQL Auth Proxy. This is how you can interact with the DB on your local machine but with a proxy layer. Follow this [article](https://cloud.google.com/sql/docs/mysql/connect-auth-proxy#unix-sockets).

7. Run `gcloud sql instances describe my-database-instance --format='value(connectionName)'`

8. Make cloudsql directory within `handy-dynamics` repo through running `sudo mkdir /cloudsql`

9. Run `sudo chmod 777 /cloudsql`

10. Run `./cloud-sql-proxy handy-bot:us-east1:my-database-instance`. You should be seeing "running on 127.0.0.1:5432 if things are wokring. Here, the DB is running locally!

### One-time repo setup

1. Install `uv` if you don't have it yet. Follow this [article](https://docs.astral.sh/uv/getting-started/installation/)
2. `uv sync` while in `~/handy-dynamics`
3. `source .venv/bin/activate`
4. Run API via `python -m api.main`. You should be able to navigate to `127.0.0.1:8000/docs`
5. Try making get requests to the endpoints you see
