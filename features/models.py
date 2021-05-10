from django.db import models


class Slider(models.Model):
    image = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)


class Banner(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)


class Partners(models.Model):
    logo = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=50)


class supporters(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
