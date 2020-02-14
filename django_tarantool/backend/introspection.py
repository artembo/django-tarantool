from django.db.backends.base.introspection import (
    BaseDatabaseIntrospection, TableInfo,
)


class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse = {
        'bool': 'BooleanField',
        'boolean': 'BooleanField',
        'smallint': 'SmallIntegerField',
        'smallint unsigned': 'PositiveSmallIntegerField',
        'smallinteger': 'SmallIntegerField',
        'int': 'IntegerField',
        'integer': 'IntegerField',
        'bigint': 'BigIntegerField',
        'integer unsigned': 'PositiveIntegerField',
        'decimal': 'DecimalField',
        'real': 'FloatField',
        'text': 'TextField',
        'char': 'CharField',
        'varchar': 'CharField',
        'blob': 'BinaryField',
        'date': 'DateField',
        'datetime': 'DateTimeField',
        'time': 'TimeField',
    }

    def get_constraints(self, cursor, table_name):
        pass

    def get_key_columns(self, cursor, table_name):
        pass

    def get_sequences(self, cursor, table_name, table_fields=()):
        pass

    def get_table_list(self, cursor):
        """Return a list of table and view names in the current database."""
        spaces = cursor.execute('SELECT * FROM "_space"')

        return [TableInfo(table[2], 't') for table in spaces if not table[2].startswith('_')]
