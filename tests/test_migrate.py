from django.test import TestCase

from django_sb_simple_migrations.management.commands.migrate import (
    Command as MigrateCommand,
)


class SimpleMigrationsTestCase(TestCase):
    command = MigrateCommand
