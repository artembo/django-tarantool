# Django Tarantool database backend

[![Build Status](https://travis-ci.com/artembo/django-tarantool.svg?branch=master)](https://travis-ci.com/artembo/django-tarantool)
[![Build Status](https://img.shields.io/pypi/v/django-tarantool.svg?color=blue)](https://pypi.org/project/django-tarantool/)

[![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-tarantool?color=blue&label=%20&logo=django)](https://www.djangoproject.com/)

## Installation

Install Tarantool v2.2+. See the installation manual for your OS [here](https://www.tarantool.io/en/download/)

Make a database directory and run Tarantool instance there:

```bash
$ mkdir ~/project_db
$ cd ~/project_db
$ tarantool
```

You will see the Tarantool interpreter. Initialize DB configuration and create password for *admin*

```
tarantool> box.cfg({ listen = 3301 })
tarantool> box.schema.user.passwd('admin', 'password')
```

To get started with django-tarantool, run the following in a virtual environment:

```bash
pip install django-tarantool
```

Add ``DATABASES`` config of your Tarantool into ``settings.py``

```python
DATABASES = {
    'default': {
        'ENGINE': 'django_tarantool.backend',
        'HOST': '127.0.0.1',
        'PORT': '3301',
        'USER': 'admin',
        'PASSWORD': 'password',
        'CONN_MAX_AGE': 3600,
    }
}
```

Mind using *CONN_MAX_AGE* param as very important. It allows to keep connection opened for the specified time in
seconds. Otherwise, Django will open the connection to the Tarantool instance on each request and close after it, which
increases the request latency.

Run `migrate` as usual:

```bash
python manage.py migrate
```

Run Django development server:

```bash
python manage.py runserver 0:8000
```
