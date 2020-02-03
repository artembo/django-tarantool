# Django tarantool database backend
Very first version

Installation

Install tarantool-python with dbapi2 on board.  
Now it is hosted at https://github.com/artembo/tarantool-python/tree/dbapi2 

```shell script
pip install git+https://github.com/artembo/tarantool-python@dbapi2 
```

Add ``DATABASES`` config of your Tarantool into ``settings.py``
```python
DATABASES = {
    'default': {
        'ENGINE': 'django_tarantool.tarantool_backend',
        'HOST': '127.0.0.1',
        'PORT': '3301',
        'USER': 'admin',
        'PASSWORD': 'password',
        'ATOMIC': True,
    }
}
```


### Limitations:

- altering tables is not supported (need to squash existed migrations or remove it and make again)
- transactions are not supported (only atomic)


