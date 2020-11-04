from django.db.backends.base.features import BaseDatabaseFeatures
from django.utils.functional import cached_property


class DatabaseFeatures(BaseDatabaseFeatures):
    uses_savepoints = False
    can_alter_table_rename_column = False
    can_introspect_autofield = True  #
    can_introspect_big_integer_field = False
    can_introspect_binary_field = False  #
    can_introspect_decimal_field = False  #
    can_introspect_duration_field = False  #
    can_introspect_ip_address_field = False  #
    can_introspect_time_field = False  #

    max_query_params = 65000

    @cached_property
    def supports_transactions(self):
        return False
