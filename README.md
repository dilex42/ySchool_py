## ySchool_py
Yalantis Python School test task
___
URLs
- **/api/courses/** API (DRF)
- **/docs/** Docs (Swagger UI)

# Run via docker-compose
### Build 
`docker-compose build`

### Run tests
`docker-compose run backend_django ./manage.py test`

### Run dev server
`docker-compose up`

# Run via venv
### Create venv
`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`


### Run tests
`./manage.py test`

### Run dev server
`./manage.py runserver 0.0.0.0:8000`
