# Django tarantool database backend
Very first version

Installation

Install tarantool-python with dbapi2 on board.  
Now it is hosted at https://github.com/artembo/tarantool-python/tree/dbapi2 

```
pip install git+https://github.com/artembo/tarantool-python@dbapi2 
```

### Limitations:

- altering tables not supported (need to squash existed migrations or remove it and make again)
- transactions is not supported (only atomic)


