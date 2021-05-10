# Generated by Django 3.2.2 on 2021-05-10 19:46

import authentication.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Leader'), (3, 'Member'), (4, 'Judge')], help_text='is Admin , Leader , Member or Judge')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authentication.user')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('f_name', models.CharField(max_length=128)),
                ('l_name', models.CharField(max_length=128)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=11)),
                ('mobile', models.CharField(max_length=11, unique=True)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(max_length=256)),
                ('ldc', models.CharField(max_length=128)),
                ('major', models.CharField(max_length=128)),
                ('orientation', models.CharField(max_length=128)),
                ('Country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('password', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
