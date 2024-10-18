# FastAPI Template

## Overview

This project is a backend service built with Docker Compose, providing various tools to facilitate development, testing, and code quality checks. The project includes integration with tools like `pytest`, `bandit`, `black`, `flake8`, and `mypy` for testing, security scanning, formatting, and linting, respectively.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1. Clone the repository:
    ```bash
    git clone <git@github.com:chingmanle/fastapi-template.git>
    cd <fastapi-template>
    ```

2. Copy the `.env` file:
    ```bash
    make copy-env
    ```

3. Build the Docker containers:
    ```bash
    make build
    ```

## Usage

### Start the Backend

To start the backend in the background:

```bash
make up
```

To stop the backend:

```bash
make stop
```

To shut down the backend completely:

```bash
make down
```

## Running Tests

### Pytest

Run tests using `pytest`:

```bash
make pytest
```

### Coverage

Run tests with coverage:

```bash
make coverage
```

## Code Quality

### Bandit

Run `bandit` to check for security issues:

```bash
make bandit
```

### Black

Run `black` for code formatting:

```bash
make black
```

### Flake8

Run `flake8` for linting:

```bash
make flake8
```

### Mypy

Run `mypy` for static type checking:

```bash
make mypy
```

## Help

To see the available commands:

```bash
make help
```

This will list all the available commands with descriptions.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
