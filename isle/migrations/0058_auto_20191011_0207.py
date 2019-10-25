# Generated by Django 2.0.7 on 2019-10-10 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('isle', '0057_merge_20190723_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'isle'), ('model', 'Trace')), models.Q(('app_label', 'isle'), ('model', 'LabsEventResult')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.Event')),
            ],
        ),
        migrations.AddField(
            model_name='eventmaterial',
            name='summary',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.Summary'),
        ),
        migrations.AddField(
            model_name='eventonlymaterial',
            name='summary',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.Summary'),
        ),
        migrations.AddField(
            model_name='eventteammaterial',
            name='summary',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.Summary'),
        ),
    ]
