from django.test import TestCase
from django_sb_simple_migrations.management.commands.makemigrations import (
    Command as MakeMigrationsCommand,
)


class SimpleMigrationsTestCase(TestCase):
    command = MakeMigrationsCommand
