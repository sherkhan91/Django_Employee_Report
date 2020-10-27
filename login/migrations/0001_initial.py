# Generated by Django 3.1.1 on 2020-10-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('projectName', models.CharField(max_length=100)),
                ('projectDescription', models.CharField(max_length=800)),
                ('projectFeedback', models.CharField(max_length=500)),
            ],
        ),
    ]
