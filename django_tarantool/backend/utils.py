import time


def wait_for_tarantool(connection):
    while True:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
        except Exception as e:
            print(e)
            time.sleep(1)
            continue
        finally:
            break
