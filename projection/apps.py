from django.apps import AppConfig


class ProjectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projection'

    SAT = 0
    SUN = 1
    MON = 2
    TUE = 3
    WED = 4
    THU = 5
    FRI = 6
    WEEK_DAYS = (
        (SAT, 'sat'),
        (SUN, 'sun'),
        (MON, 'mon'),
        (TUE, 'tue'),
        (WED, 'wed'),
        (THU, 'thu'),
        (FRI, 'fri'),
    )

    AVAILABLE = 1
    UNAVAILABLE = 0
    STATUS = (
        (AVAILABLE, 'available'),
        (UNAVAILABLE, 'unavailable'),
    )
