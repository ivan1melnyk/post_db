***STEPS***

docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=myuser -d -p 5432:5432 postgres

docker exec -it some-postgres psql -U myuser

CREATE DATABASE universitydb;

Go to Terminal and do code step_1-4
