# Personal Website Backend


## MAIN used tools and concepts:
**Django** : Django is a high-level Python Web framework

**Django REST framework** : Django REST framework is a powerful and flexible toolkit for building Web APIs.

## Project structure

| File/Folder      | Description |
| ----------- | ----------- |
| pwb      | The django module       |
| pwb/run_dev   | Script to run server with dev settings        |
| pwb/run_prod   | Script to run server with prod settings        |
| pwb/run_heroku   | Script to run server with heroku settings (Same settings as prod with some added tweaks)        |
| docker   | Docker files for dev and prod        |


## How to run:
### normal mode:

1. Create python environment and install dependecies

`virtualenv env`

`source env/bin/activate`

`pip install -r full_requirements.txt`

3. Go to the django Module

`cd pwb`

4. Run the server

`./run_dev` (or `./run_prod`)

### Docker mode:

1. Build image

`docker build --tag pwb:0.1.0 -f docker/DockerfileProd .` (Or DockerfileDev)

2. run image

`docker run -p 80:80 pwb:0.1.0` (Expose the port you are using depending on dev and prod)
