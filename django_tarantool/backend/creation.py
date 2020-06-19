import os
import shutil
import subprocess
from pathlib import Path

from django.core.management import call_command
from django.db.backends.base.creation import BaseDatabaseCreation

from django_app import settings
from django_tarantool.backend.utils import wait_for_tarantool

START_LUA = """\
box.cfg({ listen = %d })
box.schema.user.passwd('admin', 'password')
"""


class DatabaseCreation(BaseDatabaseCreation):
    tarantool_proc = None
    tarantool_test_port = 3302
    db_path = None

    def _quote_name(self, name):
        return self.connection.ops.quote_name(name)

    def _prepare_db_path(self, db_name):
        path = os.path.join(settings.BASE_DIR, db_name)
        Path(path).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(path, 'start.lua'), 'w+') as file:
            file.write(START_LUA % self.tarantool_test_port)
        return path

    def start_test_tarantool(self):
        test_database_name = self._get_test_db_name()
        self.db_path = self._prepare_db_path(test_database_name)
        self.tarantool_proc = subprocess.Popen(['tarantool', 'start.lua'], cwd=self.db_path)
        wait_for_tarantool(self.connection)

    def create_test_db(self, verbosity=1, autoclobber=False, serialize=True, keepdb=False):
        settings.DATABASES[self.connection.alias]["PORT"] = self.tarantool_test_port
        self.connection.settings_dict["PORT"] = self.tarantool_test_port
        self.start_test_tarantool()

        call_command('migrate', 'app', interactive=False)

    def destroy_test_db(self, old_database_name=None, verbosity=1, keepdb=False, suffix=None):
        self.tarantool_proc.kill()
        super().destroy_test_db(old_database_name, verbosity, keepdb, suffix)

    def _destroy_test_db(self, test_database_name, verbosity):
        shutil.rmtree(self.db_path)
