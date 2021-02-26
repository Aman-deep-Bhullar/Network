# Generated by Django 3.1.2 on 2020-12-28 04:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20201228_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='likes',
            field=models.ManyToManyField(related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
