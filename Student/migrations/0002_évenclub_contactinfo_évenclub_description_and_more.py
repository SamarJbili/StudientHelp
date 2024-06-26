# Generated by Django 5.0.2 on 2024-05-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='évenclub',
            name='ContactInfo',
            field=models.CharField(default='example@example.com', max_length=200),
        ),
        migrations.AddField(
            model_name='évenclub',
            name='Description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='évenclub',
            name='Intitulé',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='évenclub',
            name='Lieu',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='évensocial',
            name='ContactInfo',
            field=models.CharField(default='example@example.com', max_length=200),
        ),
        migrations.AddField(
            model_name='évensocial',
            name='Description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='évensocial',
            name='Intitulé',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='évensocial',
            name='Lieu',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='évenclub',
            name='Club',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='évensocial',
            name='Prix',
            field=models.FloatField(default=0.0),
        ),
    ]
