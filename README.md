## Example of environment

Create file .env at the root of the project

```
    DATABASE_PORT=6500
    POSTGRES_PASSWORD=password123
    POSTGRES_USER=postgres
    POSTGRES_DB=books
    POSTGRES_HOST=postgres
    POSTGRES_HOSTNAME=127.0.0.1
    HOST_DB=postgres-book
    PORT=9060
```

### Command to run backend with docker

```
docker compose up --buil -d
```