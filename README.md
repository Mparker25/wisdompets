# Django README

This readme was constructed by [Malik B. Parker](mailto:malik.bernard.parker@gmail.com)  
Credits: "Learning Django" by Caleb Smith (via [LinkedIn Learning](https://www.linkedin.com/learning/learning-django-2/))

## Django Projects

Create a Django Project by doing the following:

```shell
django-admin startproject wisdompets 
```

This will create a Top-Directory 'wisdompets' which will create a subdirectory containing the following as contents:  

``` shell
.
├── manage.py
└── wisdompets
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

*Important Files*:  
manage.py - runs various commands for our project  
settings.py - configures django  
urls.py - Routes web requests based on URL  

## Running a Django Web Server

``` shell
python3 manage.py runserver 
```

Open a browser and go to [localhost:8000](http://localhost:8000). This is the **default** location for a Local Django Webserver

## Django Apps

A component within a Django Project. Each app fits a specific purpose  

Examples of apps:  

* Blog
* Forum
* Wiki
* Etc

## Creating the Django App

### Step 1: Create a Django App

To create a Django App, go to your Django project folder and use the following shell commands:

```shell
python3 manage.py startapp adoptions
```

Here we're creating an app within the 'wisdompets' Project called  "adoptions". It will create a new folder in the directory containing the following files:

```shell
.
├── adoptions
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── wisdompets
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   └── settings.cpython-39.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

*Important Files*:  

* admin.py - administrative interface for the app
* apps.py - controls settings specific to the app (rarely need to edit this)
* migrations/ - hold files to migrate that Django uses to migrate the database as we create and change the database schema overtime
* modesl.py - priovides data layer for djangi
* views.py - describes logic and control flwo for websrequestt defines the http respoinses to be returned
* tests.py - writing unit tests for the fuinctionality of the app

### Step 2: Add Django App to the Project Settings

In your project settings (settings.py), you'll need to add your newly created app to the list of installed apps.  

So for the adoptions app, we'll add it to the end of the list `INSTALLED_APPS`

<img src="Media/installed_apps_aftr.png" width=50% >

## Migrations

