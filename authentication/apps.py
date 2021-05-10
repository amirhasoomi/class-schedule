from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'

    USER_TYPE_ADMIN = 1
    USER_TYPE_LEADER = 2
    USER_TYPE_MEMBER = 3
    USER_TYPE_JUDGE = 4
    USER_TYPES = (
        (USER_TYPE_ADMIN, 'Admin'),
        (USER_TYPE_LEADER, 'Leader'),
        (USER_TYPE_MEMBER, 'Member'),
        (USER_TYPE_JUDGE, 'Judge'),
    )
