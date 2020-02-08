from _django.utils.datetime_safe import datetime
from django.db.backends.base.operations import BaseDatabaseOperations


class DatabaseOperations(BaseDatabaseOperations):

    def quote_name(self, name):
        return '"%s"' % name

    def get_db_converters(self, expression):
        converters = super().get_db_converters(expression)
        internal_type = expression.output_field.get_internal_type()
        if internal_type == 'DateTimeField':
            converters.append(self.convert_datetimefield_value)
        elif internal_type == 'DateField':
            converters.append(self.convert_datefield_value)
        elif internal_type in ('BooleanField', 'NullBooleanField'):
            converters.append(self.convert_booleanfield_value)
        return converters

    def convert_booleanfield_value(self, value, expression, connection):
        return value

    def convert_datefield_value(self, value, expression, connection):
        if value in (None, 'None'):
            return None
        return datetime.fromordinal(int(value))

    def convert_datetimefield_value(self, value, expression, connection):
        if value in (None, 'None'):
            return None
        else:
            value = datetime.fromtimestamp(int(value))
        #     if settings.USE_TZ:
        #         value = timezone.make_aware(value, self.connection.timezone)
        return value

    def bulk_insert_sql(self, fields, placeholder_rows):
        placeholder_rows_sql = (", ".join(row) for row in placeholder_rows)
        values_sql = ", ".join("(%s)" % sql for sql in placeholder_rows_sql)
        return "VALUES " + values_sql

    def adapt_datetimefield_value(self, value):
        return value.timestamp() if value else 0

    def adapt_datefield_value(self, value):
        return value.toordinal()
