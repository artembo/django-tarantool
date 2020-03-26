import uuid

from django.conf import settings
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.db.backends.base.operations import BaseDatabaseOperations
from datetime import time


class DatabaseOperations(BaseDatabaseOperations):

    def quote_name(self, name):
        return '"%s"' % name

    def pk_default_value(self):
        return 'NULL'

    def get_db_converters(self, expression):
        converters = []
        internal_type = expression.output_field.get_internal_type()
        if internal_type == 'DateTimeField':
            converters.append(self.convert_datetimefield_value)
        elif internal_type == 'DateField':
            converters.append(self.convert_datefield_value)
        elif internal_type == 'TimeField':
            converters.append(self.convert_timefield_value)
        elif internal_type == 'UUIDField':
            converters.append(self.convert_uuidfield_value)
        elif internal_type in ('BooleanField', 'NullBooleanField'):
            converters.append(self.convert_booleanfield_value)
        return converters

    def convert_booleanfield_value(self, value, expression, connection):
        return value

    def convert_datefield_value(self, value, expression, connection):
        if value is None:
            return None
        return datetime.fromtimestamp(int(value)).date()

    def convert_datetimefield_value(self, value, expression, connection):
        if value is None:
            return None
        value = datetime.fromtimestamp(value)
        if settings.USE_TZ:
            value = timezone.make_aware(value, self.connection.timezone)
        return value

    def convert_timefield_value(self, value, expression, connection):
        if value is None:
            return None
        hours, _seconds = divmod(value, 3600)
        minutes, seconds = divmod(_seconds, 60)
        return time(hours, minutes, seconds)

    def convert_uuidfield_value(self, value, expression, connection):
        if value is not None:
            value = uuid.UUID(value)
        return value

    def bulk_insert_sql(self, fields, placeholder_rows):
        placeholder_rows_sql = (", ".join(row) for row in placeholder_rows)
        values_sql = ", ".join("(%s)" % sql for sql in placeholder_rows_sql)
        return "VALUES " + values_sql

    def adapt_datetimefield_value(self, value):
        return value.timestamp() if value else None

    def adapt_datefield_value(self, value):
        return datetime.fromordinal(value.toordinal()).timestamp() if value is not None else None

    def adapt_timefield_value(self, value):
        return value.hour * 60 * 60 + value.minute * 60 + value.second if value is not None else None

    def lookup_cast(self, lookup_type, internal_type=None):
        if lookup_type in ('iexact', 'icontains', 'istartswith', 'iendswith'):
            return 'UPPER(%s)'
        return '%s'

    def no_limit_value(self):
        return 131072

    def sql_flush(self, style, tables, sequences, allow_cascade=False):
        return []
