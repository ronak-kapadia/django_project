# Generated by Django 2.2.12 on 2024-06-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('employee_id', models.IntegerField()),
                ('deparment', models.CharField(max_length=256)),
            ],
        ),
    ]
