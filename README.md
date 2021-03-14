# Installing
- Clone repository
- Go to folder `cd qumalaq`
- Install virualenv with name env `python3 -m venv env`
- Install PostgreSQL
- Create user and database in PostgreSQL, and grant all privileges `CREATE USER qumalaq WITH PASSWORD '9qumalaq@'; CREATE DATABASE qumalaq WITH OWNER qumalaq; GRANT ALL PRIVILEGES ON DATABASE qumalaq TO qumalaq`
- Run all migrations `python3 manage.py migrate`
- Start the server `python3 manage.py runserver`