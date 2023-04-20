# -*- coding: utf-8 -*-
from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models


class AppSettings:
    prefix = "SIMPLE_MIGRATIONS"
    defaults = {
        "IGNORED_ATTRS": [
            # (
            #   field type,
            #   attribute name,
            #   blacklist of field sub-types (an empty list means all subtypes)
            # )
            (
                models.Field,
                "verbose_name",
                [],
            ),
            (
                models.Field,
                "help_text",
                [],
            ),
            (
                models.Field,
                "validators",
                [],
            ),
            (
                models.Field,
                "editable",
                [
                    models.DateField,
                    models.DateTimeField,
                    models.DateField,
                    models.BinaryField,
                ],
            ),
            (
                models.Field,
                "blank",
                [
                    models.DateField,
                    models.DateTimeField,
                    models.AutoField,
                    models.NullBooleanField,
                    models.TimeField,
                ],
            ),
        ]
    }
    required_settings = []

    def __init__(self, base_settings):
        self.base_settings = base_settings

        for setting in self.required_settings:
            prefixed_name = f"{self.prefix}_{setting}"

            if not hasattr(self.base_settings, prefixed_name):
                raise ImproperlyConfigured(
                    f"The '{prefixed_name}' setting is required."
                )

    def __getattr__(self, name):
        prefixed_name = f"{self.prefix}_{name}"

        if hasattr(self.base_settings, prefixed_name):
            return getattr(self.base_settings, prefixed_name)

        if name in self.defaults:
            return self.defaults[name]

        raise AttributeError(f"'AppSettings' object does not have a '{name}' attribute")


settings = AppSettings(django_settings)
