from django.apps import AppConfig


class ProjectionConfig(AppConfig):
    name = 'projection'

    STATUS_REGISTRATED = 1
    STATUS_AGREE = 2
    STATUS_AGAINST = 3
    STATUS_PRESENT = 4
    STATUS_ACCEPT = 5
    STATUS_REJECT = 6
    STATUS_WFS = 7
    STATUS_SIGNED = 8
    STSATUS_TYPES = (
        (STATUS_REGISTRATED, 'registrated'),
        (STATUS_AGREE, 'agreed'),
        (STATUS_AGAINST, 'against'),
        (STATUS_PRESENT, 'present'),
        (STATUS_ACCEPT, 'accepted'),
        (STATUS_REJECT, 'rejected'),
        (STATUS_WFS, 'wait_for_sign'),
        (STATUS_SIGNED, 'signed')
    )
