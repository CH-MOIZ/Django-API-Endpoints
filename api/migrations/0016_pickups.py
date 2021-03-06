# Generated by Django 3.2.8 on 2021-10-07 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_delete_pickups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pickups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_location', models.CharField(max_length=200)),
                ('p_action', models.CharField(max_length=20)),
                ('p_arv_date', models.CharField(max_length=200)),
                ('p_dep_date', models.CharField(max_length=200)),
                ('dis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup', to='api.dispatches')),
            ],
        ),
    ]
