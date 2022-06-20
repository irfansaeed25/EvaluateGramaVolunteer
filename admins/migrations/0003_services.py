# Generated by Django 3.2.12 on 2022-06-16 04:06

import admins.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_auto_20220614_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('mobileNo', models.IntegerField(max_length=10, validators=[admins.models.mobileNoValidate])),
                ('aadharNo', models.IntegerField(max_length=12)),
                ('name', models.CharField(max_length=100)),
                ('serviceSelected', models.CharField(max_length=255)),
                ('requiredDocuments', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
