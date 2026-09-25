# lab-python-dotenv-guide

[![python](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

Python project demonstrating the use of `python-dotenv` for managing environment variables in different environments.

## Features

- Centralized management of environment variables using `python-dotenv`.
- Supports multiple environment configurations (development, production, local overrides).
- Easy integration with `uv` for environment-specific execution.

## Hierarchical Loading of Environment Variables

The project loads environment variables in the following order of precedence:

1. Native environment variables set in the operating system
2. `.env.<APP_ENV>.local` - Local overrides for the current environment (should not be committed to version control)
3. `.env.<APP_ENV>` - Environment-specific variables
4. `.env` - Default shared environment variables

## Quick Start

This project is managed using [uv](https://github.com/astral-sh/uv). Follow the commands below to get started:

```bash
# Install dependencies and update the lockfile
uv sync

# Execute the application using the development environment
APP_ENV=development uv run main.py

# Execute the application using the production environment
APP_ENV=production uv run main.py
```

## Project Structure

```
lab-python-dotenv-guide/
├── .env                     # Default shared environment variables
├── .env.development         # Development environment variables
├── .env.development.local   # Local overrides for development environment (should not be committed to version control)
├── .env.production          # Production environment variables
├── .env.production.local    # Local overrides for production environment (should not be committed to version control)
├── config.py                # Configuration file for environment variables and settings
├── main.py                  # Entry point of the application
├── pyproject.toml           # Project metadata and dependencies
└── uv.lock                  # uv lockfile (auto-generated)
```

## Docker

Build the Docker image:

```bash
docker build -t lab-python-dotenv-guide .
```

Run the Docker container:

```bash
# Run the Docker container with the local environment variables from the .env file
docker run -p 8000:8000 --env-file .env lab-python-dotenv-guide

# Run the Docker container with the development environment variables
docker run -p 8000:8000 -e APP_NAME=YOUR_APP_NAME lab-python-dotenv-guide
```
