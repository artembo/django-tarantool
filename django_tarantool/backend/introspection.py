from django.db.backends.base.introspection import BaseDatabaseIntrospection, TableInfo


class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse = {}

    def get_constraints(self, cursor, table_name):
        pass

    def get_key_columns(self, cursor, table_name):
        pass

    def get_sequences(self, cursor, table_name, table_fields=()):
        pass

    def get_table_list(self, cursor):
        spaces = cursor.execute('SELECT * FROM "_space"')

        return [TableInfo(table[2], 't') for table in spaces if not table[2].startswith('_')]
