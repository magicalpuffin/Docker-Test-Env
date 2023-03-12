### Notes
- bruh i dunno
- I guess there will need to be multiple versions, for local, dev, staging, prod...
- Have to build and push using ECR for dev version. Ideally only be switching out environment variables between.
- local would probably be postgres, dev will be aws rds. Some concern about difference between versions
- zappa_settings will probably be massive i guess for all of the env variables
- There will probably be many docker files

### Should figure out
- Database migrations
- Easier ways to run the handler

### Docker Files
- docker-compose will be used for creating the local test environment
- dockerfiles for dev and local. The dev docker file would be built and deployed with zappa.
- everything should be run from the root folder

### Powershell Scripts
- Used for deploying to AWS ECR
- Edit variables in other powershell file

### Environment Variables
I have like a bunch of environment variables now. The ones that get passed into the dev version are
passed in through zappa settings. There are environment variables just used for the power shell scripts.
There are environment variables passed in for the local version

## Versions
- I don't know what is the right word, there will need to be multiple different versions
### local
- Local test environment to test changes imediately
- Uses docker and docker compose. Local version of postgres running
## dev
- Deployed using zappa to a online dev instance. Used to debug any lambda issues
- Uses AWS RDS postgres database. Are on the same VPC
- Probaly needs some S3 thing for staic files
## production
- I dunno haven't made it yet

## Setup
### Postgres Database Setup
For creating and using another user instead of admin
- Create database: `CREATE DATABASE database_name;`
- Create user: `CREATE USER my_username WITH PASSWORD 'my_password';`
- Grant database privileges: `GRANT ALL PRIVILEGES ON DATABASE database_name to my_username;`
- Grant all public schema: `GRANT ALL ON SCHEMA public TO my_username;`
    - Required for Postgresql 15
    - Should be connected to the target database

### Django Database Migrations
Normally
- `python manage.py showmigrations`
- `python manage.py makemigrations`
- `python manage.py migrate`
Zappa
- `zappa manage dev showmigrations`
- `zappa manage dev makemigrations`
- `zappa manage dev migrate`