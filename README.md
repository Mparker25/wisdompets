# Getting Started Guide 

## Create a Django Project

```python
django-admin startproject [project-name]
```

## Run project Server

```python
cd [project-name]
python3 manage.py runserver
```

## Creating a webapp under the Project/Company

```python
python3 manage.py startup [webapp name]
```

## Migrations

Needs to be run to update models and views after they change.

### Make migrations
```python
python3 manage.py makemigrations
```

### Show Migrations
```python
python3 manage.py showmigrations
```

### Migrate
```python
python3 manage.py migrate
```
