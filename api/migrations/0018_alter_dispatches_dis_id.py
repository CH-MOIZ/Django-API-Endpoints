# Generated by Django 3.2.8 on 2021-10-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20211007_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatches',
            name='dis_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
