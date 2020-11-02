# Django Tarantool database backend
[![Build Status](https://travis-ci.com/artembo/django-tarantool.svg?branch=master)](https://travis-ci.com/artembo/django-tarantool)

## Installation


Install Tarantool v2 or later. See the installation manual
for your OS [here](https://www.tarantool.io/en/download/)

Make a database directory and run Tarantool instance there:

```shell script
$ mkdir ~/project_db
$ cd ~/project_db
$ tarantool
```

You will see the Tarantool interpreter. Initialize DB 
configuration and create password for *admin*

```
tarantool> box.cfg{listen = 3301}
tarantool> box.schema.user.passwd('admin', 'password')
```

Install tarantool-python with dbapi2 on board.  
Now it is hosted at https://github.com/tarantool/tarantool-python/tree/master  
**Note:** The PIP *tarantool* package will be updated soon, you'll be able
to install it with *dbapi2* module by `pip install tarantool` when 
`tarantool>0.6.6` is released.

```
pip install git+https://github.com/tarantool/tarantool-python@master#egg=tarantool 
```

To set up django-tarantool enter in the command line: 
```
pip install django-tarantool
```

Add ``DATABASES`` config of your Tarantool into ``settings.py``
```
DATABASES = {
    'default': {
        'ENGINE': 'django_tarantool.backend',
        'HOST': '127.0.0.1',
        'PORT': '3301',
        'USER': 'admin',
        'PASSWORD': 'password',
    }
}
```
Run `migrate` as usual:  
`python manage.py migrate`

Run Django develepment server:  
`python manage.py runserver 0:8000`
