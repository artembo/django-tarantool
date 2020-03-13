from django.db.backends.base.features import BaseDatabaseFeatures
from django.utils.functional import cached_property


class DatabaseFeatures(BaseDatabaseFeatures):
    uses_savepoints = False

    @cached_property
    def supports_transactions(self):
        return False
