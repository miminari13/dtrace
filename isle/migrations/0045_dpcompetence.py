# Generated by Django 2.0.7 on 2019-05-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0044_auto_20190328_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='DpCompetence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=500)),
            ],
        ),
    ]
