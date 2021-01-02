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


def strip_quotes(table_name):
    """
    Strip quotes off of quoted table names to make them safe for use in index
    names, sequence names, etc. For example '"USER"."TABLE"' (an Oracle naming
    scheme) becomes 'USER"."TABLE'.
    """
    has_quotes = table_name.startswith('"') and table_name.endswith('"')
    return table_name[1:-1] if has_quotes else table_name
