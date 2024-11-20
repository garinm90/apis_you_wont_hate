# Build APIs You Won't Hate
A [FastAPI](https://fastapi.tiangolo.com/) implementation of [Build APIs You Won't Hate
Everyone and their dog wants an API, so you should probably learn how to build them.](https://apisyouwonthate.com/books/build-apis-you-wont-hate/)

## Features
- [x] SQLModel ORM for database access
- [x] Pydantic for automatic validation 
- [x] FastAPI leveraging Pydantic to create awesome documentation via OpenAPI and Swagger
- [x] UV for blazing fast package management

## Installation

Install packages with uv.

```bash
uv sync
```

If you don't have uv yet check it out here [uv](https://docs.astral.sh/uv/)

Install it with the following command
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Project Mangement

* Create your database
```bash
uv run app-cli create-datebase
```
* Generate fixture data
```bash
uv run app-cli seed-database 
```
* Run the app
```bash
uv run fastpi dev
```