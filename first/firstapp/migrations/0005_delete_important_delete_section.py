# Generated by Django 4.2.7 on 2023-11-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_alter_important_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='important',
        ),
        migrations.DeleteModel(
            name='section',
        ),
    ]
