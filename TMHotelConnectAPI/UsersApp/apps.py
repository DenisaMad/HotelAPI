from django.apps import AppConfig


class UsersappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "UsersApp"
    def ready(self):
        import UsersApp.Signals
