# Generated by Django 3.2.2 on 2021-05-10 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_profile_specialty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Specialty',
            new_name='specialty',
        ),
    ]
