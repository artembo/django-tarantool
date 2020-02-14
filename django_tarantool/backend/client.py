import subprocess

from django.db.backends.base.client import BaseDatabaseClient


class DatabaseClient(BaseDatabaseClient):
    executable_name = 'tarantoolctl'

    @classmethod
    def settings_to_cmd_args(cls, settings_dict):
        args = [cls.executable_name]

        user = settings_dict['OPTIONS'].get('user', settings_dict['USER'])
        passwd = settings_dict['OPTIONS'].get('passwd', settings_dict['PASSWORD'])
        host = settings_dict['OPTIONS'].get('host', settings_dict['HOST'])
        port = settings_dict['OPTIONS'].get('port', settings_dict['PORT'])

        args += ["connect", "tcp://%s:%s@%s:%s" % (user, passwd, host, port)]
        return args

    def runshell(self):
        args = DatabaseClient.settings_to_cmd_args(self.connection.settings_dict)
        subprocess.run(args, check=True)

