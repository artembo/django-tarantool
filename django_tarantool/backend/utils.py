import time


def wait_for_tarantool(connection):
    while True:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
        except Exception as e:
            time.sleep(.5)
            continue
        finally:
            break
