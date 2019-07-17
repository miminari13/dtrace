# Generated by Django 2.0.7 on 2019-07-17 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0052_zendeskdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='DTraceStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_entry', models.IntegerField(default=0, verbose_name='Количество записей на мероприятия контекста')),
                ('n_run_entry', models.IntegerField(default=0, verbose_name='Количество записей на прогоны контекста')),
                ('n_personal', models.IntegerField(default=0, verbose_name='Количество персонального цс')),
                ('n_team', models.IntegerField(default=0, verbose_name='Количество командного цс')),
                ('n_event', models.IntegerField(default=0, verbose_name='Загруженные пользователем материалы мероприятия')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.Context')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DTraceStatisticsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_entry', models.IntegerField(default=0, verbose_name='Количество записей на мероприятия контекста')),
                ('n_run_entry', models.IntegerField(default=0, verbose_name='Количество записей на прогоны контекста')),
                ('n_personal', models.IntegerField(default=0, verbose_name='Количество персонального цс')),
                ('n_team', models.IntegerField(default=0, verbose_name='Количество командного цс')),
                ('n_event', models.IntegerField(default=0, verbose_name='Загруженные пользователем материалы мероприятия')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.Context')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='dtracestatistics',
            unique_together={('user', 'context')},
        ),
    ]
