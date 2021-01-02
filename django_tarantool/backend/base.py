"""
Tarantool database backend for Django.
"""


from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.validation import BaseDatabaseValidation
from django.db.backends.utils import (
    CursorDebugWrapper as BaseCursorDebugWrapper,
)

from .client import DatabaseClient                          # NOQA isort:skip
from .creation import DatabaseCreation                      # NOQA isort:skip
from .features import DatabaseFeatures                      # NOQA isort:skip
from .introspection import DatabaseIntrospection            # NOQA isort:skip
from .operations import DatabaseOperations                  # NOQA isort:skip
from .schema import DatabaseSchemaEditor                    # NOQA isort:skip


from tarantool import dbapi


Database = dbapi


class DatabaseWrapper(BaseDatabaseWrapper):
    def is_usable(self):
        return True

    vendor = 'tarantool'
    display_name = 'Tarantool'
    Database = Database
    SchemaEditorClass = DatabaseSchemaEditor
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    data_types = {
        'AutoField': 'INTEGER',
        'BigAutoField': 'INTEGER',
        'BinaryField': 'VARBINARY',
        'BooleanField': 'BOOLEAN',
        'NullBooleanField': 'BOOLEAN',
        'CharField': 'VARCHAR(%(max_length)s)',
        'TextField': 'TEXT',
        'UUIDField': 'VARCHAR(32)',
        'SlugField': 'VARCHAR(%(max_length)s)',
        'DateField': 'UNSIGNED',
        'DateTimeField': 'NUMBER',
        'TimeField': 'UNSIGNED',
        'DurationField': 'INTEGER',
        'OneToOneField': 'INTEGER',
        'FileField': 'VARCHAR(%(max_length)s)',
        'FilePathField': 'VARCHAR(%(max_length)s)',
        'BigIntegerField': 'INTEGER',
        'IntegerField': 'INTEGER',
        'PositiveIntegerField': 'UNSIGNED',
        'SmallIntegerField': 'INTEGER',
        'PositiveSmallIntegerField': 'UNSIGNED',
        'FloatField': 'NUMBER',
        'DecimalField': 'NUMBER',
        'IPAddressField': 'VARCHAR(15)',
        'GenericIPAddressField': 'VARCHAR(39)',
    }

    data_types_suffix = {
        'AutoField': 'AUTOINCREMENT',
        'BigAutoField': 'AUTOINCREMENT',
    }

    pattern_esc = r"REPLACE(REPLACE(REPLACE({}, '\', '\\'), '%%', '\%%'), '_', '\_')"
    operators = {
        'exact': '= %s',
        'iexact': "= UPPER(%s)",
        'contains': "LIKE %s",
        'icontains': "LIKE UPPER(%s)",
        'regex': 'REGEXP %s',
        'iregex': "REGEXP '(?i)' || %s",
        'gt': '> %s',
        'gte': '>= %s',
        'lt': '< %s',
        'lte': '<= %s',
        'startswith': "LIKE %s",
        'endswith': "LIKE %s",
        'istartswith': "LIKE UPPER(%s)",
        'iendswith': "LIKE UPPER(%s)",
    }

    pattern_ops = {
        'contains': r"LIKE '%%' || {} || '%%' ESCAPE '\'",
        'icontains': r"LIKE '%%' || UPPER('{}') || '%%' ESCAPE '\'",
        'startswith': r"LIKE {} || '%%' ESCAPE '\'",
        'istartswith': r"LIKE UPPER({}) || '%%' ESCAPE '\'",
        'endswith': r"LIKE '%%' || {} ESCAPE '\'",
        'iendswith': r"LIKE '%%' || UPPER({}) ESCAPE '\'",
    }

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

        self.ops = DatabaseOperations(self)
        self.features = DatabaseFeatures(self)
        self.creation = DatabaseCreation(self)
        self.introspection = DatabaseIntrospection(self)
        self.validation = BaseDatabaseValidation(self)

    def get_connection_params(self):
        settings_dict = self.settings_dict

        conn_params = {
            **settings_dict['OPTIONS'],
        }
        conn_params.pop('isolation_level', None)
        if settings_dict['USER']:
            conn_params['user'] = settings_dict['USER']
        if settings_dict['PASSWORD']:
            conn_params['password'] = settings_dict['PASSWORD']
        if settings_dict['HOST']:
            conn_params['host'] = settings_dict['HOST']
        if settings_dict['PORT']:
            conn_params['port'] = settings_dict['PORT']
        conn_params['use_list'] = False
        return conn_params

    def get_new_connection(self, conn_params):
        connection = dbapi.connect(**conn_params)
        return connection

    def _set_autocommit(self, value):
        pass

    def init_connection_state(self):
        pass

    def create_cursor(self, name=None):
        return CursorWrapper(self.connection.cursor())

    def make_debug_cursor(self, cursor):
        return CursorDebugWrapper(cursor, self)


class CursorWrapper:
    """Tarantool supports only qmark and named param styles
    the easies way to send SQL query with proper for tarantool
    parameters is to convert them to qmark style.
    We need to overwrite execute and executemany methods to do it.
    """
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query, params=()):
        query = self.convert_query(query, len(params)) if params else query
        return self.cursor.execute(query, params)

    def executemany(self, query, param_list):
        query = self.convert_query(query, len(param_list[0])) if param_list else query
        return self.cursor.executemany(query, param_list)

    def convert_query(self, query, num_params):
        return query % tuple("?" * num_params)

    def __getattr__(self, attr):
        return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)


class CursorDebugWrapper(BaseCursorDebugWrapper):
    def copy_expert(self, sql, file, *args):
        with self.debug_sql(sql):
            return self.cursor.copy_expert(sql, file, *args)

    def copy_to(self, file, table, *args, **kwargs):
        with self.debug_sql(sql='COPY %s TO STDOUT' % table):
            return self.cursor.copy_to(file, table, *args, **kwargs)
