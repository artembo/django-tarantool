from django.db.backends.base.client import BaseDatabaseClient


class DatabaseClient(BaseDatabaseClient):
    executable_name = 'tarantool'

    @classmethod
    def runshell_db(cls, conn_params):
        raise NotImplementedError

    def runshell(self):
        raise NotImplementedError
