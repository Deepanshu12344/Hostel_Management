# Generated by Django 4.2.7 on 2023-11-28 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('room_no', models.CharField(max_length=10)),
                ('room_type', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_joining', models.DateField()),
                ('course_detail', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('father_contact_no', models.CharField(max_length=15)),
                ('mother_contact_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'backup',
            },
        ),
        migrations.AlterField(
            model_name='food',
            name='date',
            field=models.DateField(),
        ),
    ]
