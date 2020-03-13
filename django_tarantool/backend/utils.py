import socket
import time

from django.db import DatabaseError
from tarantool import NetworkError


def wait_for_tarantool(connection, host='127.0.0.1', port=3302):
    port = port or port
    s = socket.socket()

    while True:
        try:
            s = s.connect((host, port))
        except socket.error:
            time.sleep(0.1)
            continue
        except Exception as e:
            print(e)
            continue
        finally:
            s.close()
            break

    # need an extra time to get up
    time.sleep(1)

    while True:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM \"_space\"")
        except (DatabaseError, NetworkError) as e:
            print(e)
            time.sleep(0.05)
            continue
        except Exception as e:
            print(e)
            continue
        finally:
            break
