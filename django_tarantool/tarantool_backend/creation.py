from django.db.backends.base.creation import BaseDatabaseCreation


class DatabaseCreation(BaseDatabaseCreation):

    def _quote_name(self, name):
        return self.connection.ops.quote_name(name)

    def _get_database_create_suffix(self, encoding=None, template=None):
        raise NotImplementedError

    def sql_table_creation_suffix(self):
        raise NotImplementedError

    def _database_exists(self, cursor, database_name):
        raise NotImplementedError

    def _clone_test_db(self, suffix, verbosity, keepdb=False):
        raise NotImplementedError
