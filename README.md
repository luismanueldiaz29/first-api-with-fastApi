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

### Command to run badatabase with docker

```
cd /docker/db
```
 
 later

```
docker compose up --buil -d
```

<p>After creating the database container, you must run the script that is located in /resources/script.sql </p>

### Command to run backend with docker

```
cd /docker/ms
```

 later

```
docker compose up --buil -d
```