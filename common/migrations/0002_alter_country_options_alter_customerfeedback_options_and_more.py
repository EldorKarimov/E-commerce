# Generated by Django 5.0.4 on 2024-05-15 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='customerfeedback',
            options={'verbose_name': 'Customer feedback', 'verbose_name_plural': 'Customer feedbacks'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Media', 'verbose_name_plural': 'Medias'},
        ),
        migrations.AlterModelOptions(
            name='ourinstagramstory',
            options={'verbose_name': 'Instagram story', 'verbose_name_plural': 'Instagram stories'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regions'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
    ]