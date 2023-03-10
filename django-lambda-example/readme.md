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