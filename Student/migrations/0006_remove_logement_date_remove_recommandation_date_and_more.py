# Generated by Django 5.0.3 on 2024-05-19 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_remove_like_content_comment_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logement',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='recommandation',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='évenclub',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='évensocial',
            name='Date',
        ),
    ]
