# Generated by Django 2.2.4 on 2019-08-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=1000)),
                ('salary', models.IntegerField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
