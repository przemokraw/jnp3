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
3. Set up the frontend
```bash
*this is under construction*
```
4. Set up the database
```bash
./manage.py migrate
```

and you're good to go!

To run the project frontend locally follow these steps:

1. Install npm (https://docs.npmjs.com/getting-started/installing-node)
 
2. `cd fietsenrek-frontend`

3. `npm install`

4. `npm run serve`

5. Go to localhost:3000
