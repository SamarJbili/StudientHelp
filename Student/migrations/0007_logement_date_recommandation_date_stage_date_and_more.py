# Generated by Django 5.0.3 on 2024-05-19 08:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_remove_logement_date_remove_recommandation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logement',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recommandation',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='stage',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='transport',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='évenclub',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='évensocial',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
