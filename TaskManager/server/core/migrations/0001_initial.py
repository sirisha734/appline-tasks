# Generated by Django 4.2.3 on 2023-07-31 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('assigned_date', models.DateField(default=datetime.date.today)),
                ('due_date', models.DateField(default=datetime.date.today)),
                ('priority_level', models.CharField(max_length=10)),
            ],
        ),
    ]