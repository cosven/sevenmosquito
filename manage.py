#!/usr/bin/env python
import os
import sys

from pymysql import install_as_MySQLdb
install_as_MySQLdb()


def mysqldb_escape(value, conv_dict):
    from pymysql.converters import encoders
    vtype = type(value)
    # note: you could provide a default:
    # PY2: encoder = encoders.get(vtype, escape_str)
    # PY3: encoder = encoders.get(vtype, escape_unicode)
    encoder = encoders.get(vtype)
    return encoder(value)


import pymysql
setattr(pymysql, 'escape', mysqldb_escape)
del pymysql


if __name__ == "__main__":
    if os.environ.get('SEMO_ENV') == 'production':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "semo.production_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "semo.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
