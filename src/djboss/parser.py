# -*- coding: utf-8 -*-

import argparse

import djboss


PARSER = argparse.ArgumentParser(
    prog = 'djboss',
    description = "Run django-boss management commands.",
    epilog = """
    To discover sub-commands, djboss first finds and imports your Django
    settings. The DJANGO_SETTINGS_MODULE environment variable takes precedence,
    but if unspecified, djboss will look for a `settings` module in the current
    directory.

    Commands should be defined in a `commands` submodule of each app. djboss
    will search each of your INSTALLED_APPS for management commands.""",
)


PARSER.add_argument('--version', action='version', version=djboss.__version__)
PARSER.add_argument('--no-eventlet', action="store_true")
PARSER.add_argument('--blocking-detection', action="store_true")

PARSER.add_argument('-l', '--log-level', metavar='LEVEL',
    default='WARN', choices='DEBUG INFO WARN ERROR'.split(),
    help="Choose a log level from DEBUG, INFO, WARN or ERROR "
         "(default: %(default)s)")

SUBPARSERS = PARSER.add_subparsers(dest='command', title='commands', metavar='COMMAND')
