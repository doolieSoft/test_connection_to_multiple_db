from django.apps import AppConfig


class ExistingDbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'existing_db'
