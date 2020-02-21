from django.db.backends.base.schema import BaseDatabaseSchemaEditor


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):

    def quote_value(self, value):
        pass

    def prepare_default(self, value):
        pass
