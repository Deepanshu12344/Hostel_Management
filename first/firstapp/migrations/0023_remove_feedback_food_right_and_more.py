# Generated by Django 5.0.2 on 2024-04-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0022_remove_feedback_ques1_remove_feedback_ques2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='food_right',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='food_wrong',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='housekeeping_right',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='housekeeping_wrong',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='internet_right',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='internet_wrong',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='maintenance_right',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='maintenance_wrong',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='security_right',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='security_wrong',
        ),
        migrations.AddField(
            model_name='feedback',
            name='ques1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='feedback',
            name='ques2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='feedback',
            name='ques3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='feedback',
            name='ques4',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='feedback',
            name='suggestions',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=''),
        ),
    ]
