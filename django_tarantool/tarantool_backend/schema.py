from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.backends.ddl_references import IndexColumns
from django.db.backends.utils import strip_quotes


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):

    def quote_value(self, value):
        pass

    def prepare_default(self, value):
        pass

    def create_model(self, model):
        super().create_model(model)
