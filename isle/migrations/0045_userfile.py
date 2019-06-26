# Generated by Django 2.0.7 on 2019-04-16 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0044_auto_20190328_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('activity_uuid', models.CharField(default='', max_length=255)),
                ('file', models.FileField(max_length=300, upload_to='')),
                ('data', jsonfield.fields.JSONField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
