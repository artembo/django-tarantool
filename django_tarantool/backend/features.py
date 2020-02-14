from django.db.backends.base.features import BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    uses_savepoints = False

    def supports_transactions(self):
        return False
