from django.db import models
from authentication.models import User


class proposal (models.Model):
    unique_code = models.CharField(unique=True, max_length=10)
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    leader = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User, related_name="member")
    file = models.FileField(upload_to='files')
    judges = models.ManyToManyField(User, related_name="judge")
    register_date = models.DateTimeField(auto_now_add=True)
    check_date = models.DateField()
    assent_date = models.DateField()
    present_date = models.DateField()
    accept_date = models.DateField()
    aontract_date = models.DateField()
    ip_address = models.CharField(max_length=15)
