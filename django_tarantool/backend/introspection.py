from django.db.backends.base.introspection import BaseDatabaseIntrospection, \
    TableInfo


class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse = {}

    def get_constraints(self, cursor, table_name):
        constraints = {}
        cursor.execute("""
        SELECT
            CAST(NULL AS STRING) AS constraint_catalog,
            CAST(NULL AS STRING) AS constraint_schema,
            "name" AS constraint_name,
            (SELECT "name" FROM "_vspace" x WHERE x."id" = y."id") AS 
            table_name,
            CASE WHEN "iid" = 0 THEN 'PRIMARY' ELSE 'UNIQUE' END AS 
            constraint_type,
            CAST(NULL AS STRING) AS initially_deferrable,
            CAST(NULL AS STRING) AS deferred,
            CAST(NULL AS STRING) AS enforced,
            "id" AS id,
            "iid" AS iid,
            "type" AS index_type
        FROM "_vindex" y
        WHERE _table_constraints_opts_unique("opts") = TRUE AND table_name = 
        '%s';
        """ % table_name)

        for constraint_catalog, constraint_schema, index, \
            table_name, constraint_type, initially_deferrable, deferred, \
            enforced, _id, iid, index_type \
                in cursor.fetchall():
                constraints[index] = {
                    "columns": [],
                    "primary_key": constraint_type == 'PRIMARY',
                    "unique": constraint_type == 'UNIQUE',
                    "foreign_key": None,
                    "check": False,
                    "index": False,
                }
                cursor.execute('PRAGMA index_info("%s"."%s")' %
                               (table_name, index))
                for constraint_data in cursor.fetchall():
                    constraints[index]['columns'].append(constraint_data[2])
        return constraints

    def get_key_columns(self, cursor, table_name):
        pass

    def get_sequences(self, cursor, table_name, table_fields=()):
        pass

    def get_table_list(self, cursor):
        spaces = cursor.execute('SELECT * FROM "_space"')

        return [TableInfo(table[2], 't') for table in spaces if
                not table[2].startswith('_')]
