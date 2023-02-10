Flask-PostgreSQL web app for renting your pet out.

To create the PostgreSQL database, open PostgreSQL in the terminal using:

```
psql
```

Then to create the database:

```
CREATE DATABASE pet_rent_db;
```

Then create a user to interact with the database:

```
CREATE USER db_dev WITH PASSWORD 'db_dev';
```

Finally, grant permissions to the database:

```
GRANT ALL PRIVILEGES ON DATABASE pet_rent_db TO db_dev;
```

Now you can use the provided `.env` to develop the database.

To drop, create and seed the database, run the Flask app and make a `get request` to `http://127.0.0.1:8002/erase/`. In the future I will change this to a CLI command but for development this makes it easy to quickly reset the database.