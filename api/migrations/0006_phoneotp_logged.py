# Generated by Django 3.2.8 on 2021-10-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211006_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneotp',
            name='logged',
            field=models.BooleanField(default=False),
        ),
    ]
