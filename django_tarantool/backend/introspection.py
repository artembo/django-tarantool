from collections import namedtuple

from django.db.backends.base.introspection import BaseDatabaseIntrospection, \
    TableInfo, FieldInfo as BaseFieldInfo


FieldInfo = namedtuple('FieldInfo', BaseFieldInfo._fields + ('pk',))


class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse = {
        'bool': 'BooleanField',
        'boolean': 'BooleanField',
        'integer': 'IntegerField',
        'number': 'FloatField',
        'unsigned': 'PositiveIntegerField',
        'decimal': 'DecimalField',
        'text': 'TextField',
        'string': 'CharField',
        'varchar': 'CharField',
    }

    def get_field_type(self, data_type, description):
        field_type = super().get_field_type(data_type, description)
        if description.pk and field_type in {'BigIntegerField', 'IntegerField',
                                             'SmallIntegerField'}:
            return 'AutoField'
        return field_type

    def get_constraints(self, cursor, table_name):
        """
        Retrieve any constraints or keys (unique, pk, fk, check, index)
        across one or more columns.

        Return a dict mapping constraint names to their attributes,
        where attributes is a dict with keys:
         * columns: List of columns this covers
         * primary_key: True if primary key, False otherwise
         * unique: True if this is a unique constraint, False otherwise
         * foreign_key: (table, column) of target, or None
         * check: True if check constraint, False otherwise
         * index: True if index, False otherwise.
         * orders: The order (ASC/DESC) defined for the columns of indexes
         * type: The type of the index (btree, hash, etc.)
        """

        constraints = {}
        cursor.execute("""
            SELECT
                "name" AS constraint_name,
                (SELECT "name" FROM "_vspace" x WHERE x."id" = y."id") AS 
                table_name,
                CASE WHEN "iid" = 0 THEN 'PRIMARY' ELSE 'UNIQUE' END AS 
                constraint_type,
                "id" AS id,
                "iid" AS iid,
                "type" AS index_type
            FROM "_vindex" y
            WHERE table_name = %s;""", [table_name])

        for index, table_name, constraint_type, _id, iid, index_type \
                in cursor.fetchall():

            constraints[index] = {
                "columns": [],
                "primary_key": constraint_type == 'PRIMARY',
                "unique": constraint_type == 'UNIQUE',
                "foreign_key": None,
                "check": False,
                "index": False,
            }
            cursor.execute('PRAGMA index_info(%s.%s)' % (
                self.connection.ops.quote_name(table_name),
                self.connection.ops.quote_name(index)
            ))

            for constraint_data in cursor.fetchall():
                constraints[index]['columns'].append(constraint_data[2])

        cursor.execute(
            'PRAGMA foreign_key_list(%s)' % self.connection.ops.quote_name(
                table_name))
        for row in cursor.fetchall():
            # Remaining on_update/on_delete/match values are of no interest.
            id_, _, table, from_, to = row[:5]
            constraints['fk_%d' % id_] = {
                'columns': [from_],
                'primary_key': False,
                'unique': False,
                'foreign_key': (table, to),
                'check': False,
                'index': False,
            }
        cursor.execute("""
        SELECT
            "name" AS constraint_name,
            "code" AS check_clause,
            (SELECT "name" FROM "_vspace" x WHERE x."id" = y."space_id") AS 
            table_name,
            "language" AS language,
            "is_deferred" AS is_deferred,
            "space_id" AS space_id
        FROM "_ck_constraint" y
        WHERE table_name = %s;""", [table_name])
        for row in cursor.fetchall():
            constraint_name = row[0]
            constraints[constraint_name] = {
                'columns': [],
                'primary_key': False,
                'unique': False,
                'foreign_key': None,
                'check': True,
                'index': False,
            }
        return constraints

    def get_relations(self, cursor, table_name):
        """
        Return a dictionary of {field_name: (field_name_other_table,
        other_table)} representing all relationships to the given table.
        """
        # Dictionary of relations to return
        relations = {
            key[0]: (key[2], key[1])
            for key in self.get_key_columns(cursor, table_name)
        }

        return relations

    def get_table_description(self, cursor, table_name):
        """
        Return a description of the table with the DB-API cursor.description
        interface.
        """
        cursor.execute('PRAGMA table_info(%s)' % self.connection.ops.quote_name(
            table_name))
        return [
            FieldInfo(
                name, data_type, None, None, None, None,
                not notnull, default, pk == 1,
            )
            for cid, name, data_type, notnull, default, pk in cursor.fetchall()
        ]

    def get_key_columns(self, cursor, table_name):
        """
        Return a list of (column_name, referenced_table_name,
        referenced_column_name)
        for all key columns in given table.
        """
        cursor.execute(
            'PRAGMA foreign_key_list(%s)' % self.connection.ops.quote_name(
                table_name))
        key_columns = []
        for _, _, referenced_table_name, column_name, referenced_column_name,\
            _, _, _ in cursor.fetchall():
            key_columns.append(
                [column_name, referenced_table_name, referenced_column_name])
        return key_columns

    def get_sequences(self, cursor, table_name, table_fields=()):
        """
        Return a list of introspected sequences for table_name. Each sequence
        is a dict: {'table': <table_name>, 'column': <column_name>}. An optional
        'name' key can be added if the backend supports named sequences.
        """
        pk_col = self.get_primary_key_column(cursor, table_name)
        return [{'table': table_name, 'column': pk_col}]

    def get_table_list(self, cursor):
        cursor.execute('SELECT "name" FROM "_space" '
                       'WHERE "name" NOT LIKE \'X_%\' ESCAPE \'X\'')

        return [TableInfo(table[0], 't') for table in cursor.fetchall()]
