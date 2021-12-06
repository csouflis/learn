# Django CRUD Example Apps

This is a small Django project to demonstrate Django CRUD functionality, it
consist of 4 small applications:

- cars\_cbv: Implement CRUD using CBV (Class Based Views).
- cars\_fbv: Implement CRUD using FBV (Function Based Views).
- cars\_fbv\_user: add user interaction to cars\_fbv example.
- cars\_gcbv\_user: add user interaction to cars\_cbv example and even more simplified with DRF generics.


## Install Required Packages

Only need Django Rest Framework and Django:

    pip install -r requirements.txt

## Running the Application

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you can run the development web server:

    ./manage.py runserver

To access the applications go to the URL <http://localhost:8000/>


## Make a user for access

Create a user using the following command:

    ./manage.py createsuperuser

To create a normal user (non super user), you must login to the admin page and
create it: <http://localhost:8000/admin/>
