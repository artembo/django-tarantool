import os
import shutil
import subprocess
import time
from pathlib import Path

from django.core.management import call_command
from django.db.backends.base.creation import BaseDatabaseCreation

from django_app import settings


class DatabaseCreation(BaseDatabaseCreation):
    tarantool_process = None
    db_path = None

    def _quote_name(self, name):
        return self.connection.ops.quote_name(name)

    def _prepare_db_path(self, db_name):
        path = os.path.join(settings.BASE_DIR, db_name)
        Path(path).mkdir(parents=True, exist_ok=True)
        return path

    def start_test_tarantool(self):
        test_database_name = self._get_test_db_name()
        self.db_path = self._prepare_db_path(test_database_name)
        self.tarantool_process = subprocess.Popen(['tarantool', 'start.lua'], cwd=self.db_path)
        time.sleep(1)

    def create_test_db(self, verbosity=1, autoclobber=False, serialize=True, keepdb=False):
        settings.DATABASES[self.connection.alias]["PORT"] = 3302
        self.connection.settings_dict["PORT"] = 3302
        self.start_test_tarantool()

        call_command('migrate', interactive=False)

    def destroy_test_db(self, old_database_name=None, verbosity=1, keepdb=False, suffix=None):
        super().destroy_test_db(old_database_name, verbosity, keepdb, suffix)
        self.tarantool_process.kill()

    def _destroy_test_db(self, test_database_name, verbosity):
        print(test_database_name)
        print(self.db_path)
        # shutil.rmtree()

