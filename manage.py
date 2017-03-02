#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys


if __name__ == "__main__":

    print('manage.py')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line
    print(sys.argv)
    execute_from_command_line(sys.argv)