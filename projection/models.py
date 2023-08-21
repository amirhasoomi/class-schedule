from django.db import models
from authentication.models import Profile
from .apps import ProjectionConfig as conf


class Field(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, unique=True)


class Plato(models.Model):
    building = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    capacity = models.IntegerField()


class Lesson(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=10, unique=True)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    theory_course = models.IntegerField()
    practical_course = models.IntegerField()


class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    date_of_week = models.PositiveSmallIntegerField(choices=conf.WEEK_DAYS)
    plato = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    professor = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()
    exam_name = models.CharField(max_length=128, null=True)
    exam_date = models.DateField(null=True)
    exam_start_time = models.TimeField(null=True)
    exam_end_time = models.TimeField(null=True)
    exam_location = models.CharField(max_length=128, null=True)


class Availability(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    date_of_week = models.PositiveSmallIntegerField(choices=conf.WEEK_DAYS)
    professor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
