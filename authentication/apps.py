from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'

    USER_TYPE_ADMIN = 1
    USER_TYPE_MEMBER = 2
    USER_TYPE_JUDGE = 3
    USER_TYPES = (
        (USER_TYPE_ADMIN, 'admin'),
        (USER_TYPE_MEMBER, 'member'),
        (USER_TYPE_JUDGE, 'judge'),
    )
