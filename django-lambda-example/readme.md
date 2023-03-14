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

## AWS Services
- lambda
    - Zappa is used to create and update AWS Lambda functions using images in ECR
    - Zappa also sets up API for calling the AWS Lambda function
    - The Lambda function must be using the same VPC as RDS
- ecr (Elastic Container Registery)
    - Used for storing containers to be deployed with AWS Lambda
- rds (Relational Database Service)
    - AWS RDS used to create and manage the database. Used for the Postgres database.
    - Database is added to a VPC. To connect using psql, ip address of local must be added
    to security group for inbound and outbound
    - Similar to EC2 but more managed databases
- s3 (Simple Storage Service)
    - Also temporarily used by Zappa
    - Used for serving static files
    - Required adding s3 gateway as an endpoint to VPC
    - Object ownership must have ACLs enabled
    - Need to modify CORS to allow content to be retrieved form S3
- vpc (Virtual Private Cloud)
    - For secure connections between services
- api gateway
    - Used to call the lambda function from a url

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
### Zappa Commands
- Check Status: `zappa status dev`
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

### Django Static Files
Normally
- `python manage.py collectstatic --noinput`
Zappa
- `zappa manage dev "collectstatic --noinput"`
    - Note that lambda must be up to date