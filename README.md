![Community-Project](https://gitlab.com/softbutterfly/open-source/open-source-office/-/raw/master/banners/softbutterfly-open-source--banner--community-project.png)

![PyPI - Supported versions](https://img.shields.io/pypi/pyversions/django-sb-simple-migrations)
![PyPI - Package version](https://img.shields.io/pypi/v/django-sb-simple-migrations)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-sb-simple-migrations)
![PyPI - MIT License](https://img.shields.io/pypi/l/django-sb-simple-migrations)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cbdc556a2ca246d2b906dfc5e1195541)](https://app.codacy.com/gl/softbutterfly/django-sb-simple-migrations/dashboard?utm_source=gl&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/cbdc556a2ca246d2b906dfc5e1195541)](https://app.codacy.com/gl/softbutterfly/django-sb-simple-migrations/dashboard?utm_source=gl&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

# Django Simple Migrations

Django migrations without unnecesary change alert triggers.

This project was originally taken from [Pretix source code](https://github.com/pretix/pretix/tree/master/src/pretix/base/management/commands) and battle testet across many projects on [SoftButterfly](https://softbutterfly.io).

This package overrides the commands `makemigrations` and `migrate`, mainly to make that `makemigrations` doesn't create migrations on non-significant database model fields and avoid `migrate` warnings. As is stated in the source code

* `makemigrations`

  > Django, for theoretically very valid reasons, creates migrations for *every single thing* we change on a model. Even the `help_text`! This makes sense, as we don't know if any database backend unknown to us might actually use this information for its database schema.
  >
  > However, many projects only supports PostgreSQL, MySQL, MariaDB and SQLite and we can be pretty certain that some changes to models will never require a change to the database. In this case, not creating a migration for certain changes will save us some performance while applying them *and* allow for a cleaner git history. Win-win!
  >
  > Only caveat is that we need to do some dirty monkeypatching to achieve it...

* `migrate`

  > Django tries to be helpful by suggesting to run "makemigrations" in red font on every "migrate" run when there are things we have no migrations for. Usually, this is intended, and running "makemigrations" can really screw up the environment of a user, so we want to prevent novice users from doing that by going really dirty and filtering it from the output.

## Requirements

- Python 3.8, 3.9, 3.10

## Install

```bash
pip install django-sb-simple-migrations
```

## Usage

Just add `django_sb_simple_migrations` to your `INSTALLED_APPS` settings

```
INSTALLED_APPS = [
  # ...
  "django_sb_simple_migrations",
  # ...
]
```

## Docs

- [Ejemplos](https://gitlab.com/softbutterfly/open-source/django-sb-simple-migrations/-/wikis)
- [Wiki](https://gitlab.com/softbutterfly/open-source/django-sb-simple-migrations/-/wikis)

## Changelog

All changes to versions of this library are listed in the [change history](CHANGELOG.md).

## Development

Check out our [contribution guide](CONTRIBUTING.md).

## Contributors

See the list of contributors [here](https://gitlab.com/softbutterfly/open-source/django-sb-simple-migrations/-/graphs/develop).
