# Generated by Django 2.1.15 on 2020-05-14 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_notificationsuser'),
        ('pittsburgh', '0002_pittsburghperson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pittsburghperson',
            name='person_ptr',
        ),
        migrations.DeleteModel(
            name='PittsburghPerson',
        ),
    ]
