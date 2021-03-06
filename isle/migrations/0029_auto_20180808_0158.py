# Generated by Django 2.0.7 on 2018-08-07 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0028_eventblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_type', models.SmallIntegerField(blank=True, choices=[(1, 'Автор интересных вопросов'), (2, 'Другое'), (3, 'Результаты тестов'), (4, 'Результат выполнения'), (5, 'Лидер мнений'), (6, 'Презентация с оценкой ведущего'), (7, 'Результаты эксперимента'), (8, 'Обратная связь участников (start-stop-continue)'), (9, 'Обратная связь тьютора\\ментора (start-stop-continue)')], null=True, verbose_name='Тип результата')),
                ('rating', models.SmallIntegerField(blank=True, choices=[(1, 'слабый результат'), (2, 'нормальный результат'), (3, 'отличный результат')], null=True, verbose_name='Оценка')),
                ('competences', models.CharField(blank=True, default='', max_length=300, verbose_name='Продемонстрированные компетенции')),
                ('result_comment', models.CharField(blank=True, default='', max_length=1000, verbose_name='Комментарии сборщика')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='eventblock',
            name='block_type',
            field=models.SmallIntegerField(choices=[(1, 'Лекция с вопросами из зала'), (3, 'Лекция с проверкой усвоения'), (4, 'Мастер-класс/освоение инструмента'), (5, 'Мастер-класс\\тренинг без фиксации'), (6, 'Работа над проектами \\ групповая работа'), (7, 'Решение кейсов'), (8, 'Стратегическая сессия \\ форсайт'), (9, 'Игра \\ модельная сессия'), (10, 'Хакатон \\ дизайн сессия'), (11, 'Нетворкинг - сессия'), (12, 'Обсуждение \\ дискуссия'), (13, 'Питч сессия \\ презентация результатов'), (14, 'Проведение эксперимента'), (15, 'Менторская \\ тьюторская сессия'), (16, 'Другое')]),
        ),
        migrations.AlterField(
            model_name='eventmaterial',
            name='trace',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.Trace'),
        ),
        migrations.AlterField(
            model_name='eventonlymaterial',
            name='trace',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.Trace'),
        ),
        migrations.AlterField(
            model_name='eventteammaterial',
            name='trace',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.Trace'),
        ),
        migrations.AddField(
            model_name='eventmaterial',
            name='result',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.UserResult'),
        ),
    ]
