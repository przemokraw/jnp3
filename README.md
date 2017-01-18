[![Build Status](https://travis-ci.org/martarozek/jnp3.svg?branch=master)](https://travis-ci.org/martarozek/jnp3)

# Fietsenrek
Team project for a university course: designing highly efficient web services

_Fietsenrek_ means a bike rack in Dutch. The project is about getting
more _fietsenrekken_ in places where they are really needed. 
It's community-based: users submit places where a bike rack would be
handy while others vote for it.

To run the project backend locally follow these steps:

1. Create a virtualenv with Python 3.5 (we suggest using a virtualenvwrapper)
    ```bash
    mkvirtualenv -p python3.5 fietsenrek
    ```
2. Install local requirements (while in the virtualenv)
    ```bash
    pip install -r requirements/local.txt
    ```
4. Set up the database
    ```bash
    ./manage.py migrate
    ```
5. Create a superuser
    ```bash
    ./manage.py createsuperuser
    ```
6. Run the development server on localhost (it's needed for the social apps)
    ```bash
    ./manage.py runserver localhost:8000
    ```
7. Add social app integrations:
    * **for Facebook**: go to [the developers site](https://developers.facebook.com/apps/237608516653103/dashboard/)
        and create a Facebook Social App in the Django admin using App ID and 
        App Secret from the site.
 

To run the project frontend locally follow these steps:

1. Install npm (https://docs.npmjs.com/getting-started/installing-node)
 
2. `cd fietsenrek-frontend`

3. `npm install`

4. `npm install @angular/http` (may require additional libraries, install them if so)

5. `npm run serve`

6. Go to localhost:3000

and you're good to go!
