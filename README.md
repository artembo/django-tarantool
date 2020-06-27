# Django Tarantool database backend
Very first version

Installation


Install Tarantool v2 or later. See the installation manual
for your OS [here](https://www.tarantool.io/en/download/)

Make a database directory and run tarantool instance there:

```shell script
mkdir project_db
cd project_db
tarantool
```

You will see tarantool interpreter
```lua
tarantool> box.cfg{listen = 3301}
tarantool> box.schema.user.passwd('admin', 'parol')
```

Install tarantool-python with dbapi2 on board.  
Now it is hosted at https://github.com/artembo/tarantool-python/tree/dbapi2 

```shell script
pip install git+https://github.com/artembo/tarantool-python@dbapi2 
```

To set up django-tarantool enter in the command line 
```shell script
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
    }
}
```
