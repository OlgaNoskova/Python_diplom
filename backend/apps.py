from django.apps import AppConfig


class BackendConfig(AppConfig):
    verbose_name = 'Настройки магазина'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'
