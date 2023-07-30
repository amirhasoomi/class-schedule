from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'

    USER_TYPE_ADMIN = 1
    USER_TYPE_USER = 2
    USER_TYPES = (
        (USER_TYPE_ADMIN, 'admin'),
        (USER_TYPE_USER, 'user'),
    )
