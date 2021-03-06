# Generated by Django 2.2.13 on 2020-10-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_auto_20201025_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.CharField(default='', max_length=255, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(default='', max_length=255, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='application',
            name='pronouns',
            field=models.CharField(default='', max_length=255, verbose_name='pronouns'),
        ),
    ]
