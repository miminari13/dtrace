# Generated by Django 2.0.7 on 2019-07-19 15:55

from django.db import migrations, models
import django.db.models.deletion


def create_circle_items_for_result(result_id, current_circle_items_ids, meta, metamodels, competences, CircleItem):
    real_items_ids = []
    for meta_item in meta:
        tools = meta_item.get('tools')
        if not isinstance(tools, list):
            tools = [None]
        for tool in tools:
            circle_item = CircleItem.objects.get_or_create(
                level=meta_item.get('level'),
                sublevel=meta_item.get('sublevel'),
                competence_id=competences.get(meta_item.get('competence')),
                model_id=metamodels.get(meta_item.get('model')),
                result_id=result_id,
                tool=tool,
            )[0]
            real_items_ids.append(circle_item.id)
    deleted_circle_items = set(current_circle_items_ids) - set(real_items_ids)
    if deleted_circle_items:
        CircleItem.objects.filter(id__in=deleted_circle_items).delete()
    return real_items_ids


def fix_circle_items(apps, schema):
    """
    создание CircleItem по метаданным из LabsEventResult и проставление их существующим
    объектам LabsUserResult и LabsTeamResult
    запросы в кафку не будут посылаться при выполнении миграции т.к. структура мероприятия не будет изменена
    """
    DpCompetence = apps.get_model('isle', 'DpCompetence')
    MetaModel = apps.get_model('isle', 'MetaModel')
    LabsEventResult = apps.get_model('isle', 'LabsEventResult')
    LabsUserResult = apps.get_model('isle', 'LabsUserResult')
    LabsTeamResult = apps.get_model('isle', 'LabsTeamResult')
    CircleItem = apps.get_model('isle', 'CircleItem')
    competence_uuid_to_id = dict(DpCompetence.objects.values_list('uuid', 'id'))
    model_uuid_to_id = dict(MetaModel.objects.values_list('uuid', 'id'))
    for res in LabsEventResult.objects.filter(meta__isnull=False):
        if res.meta and isinstance(res.meta, list):
            circle_items_ids = create_circle_items_for_result(
                res.id,
                list(res.circle_items.values_list('id', flat=True)),
                res.meta,
                model_uuid_to_id,
                competence_uuid_to_id,
                CircleItem,
            )
            for result_model in (LabsUserResult, LabsTeamResult):
                for result in result_model.objects.filter(result=res).iterator():
                    result.circle_items.set(circle_items_ids)


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0054_auto_20190718_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=None, null=True)),
                ('sublevel', models.IntegerField(default=None, null=True)),
                ('tool', models.TextField(default=None, null=True)),
                ('competence', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.DpCompetence')),
                ('model', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='isle.MetaModel')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circle_items', to='isle.LabsEventResult')),
            ],
        ),
        migrations.AddField(
            model_name='labsteamresult',
            name='circle_items',
            field=models.ManyToManyField(to='isle.CircleItem'),
        ),
        migrations.AddField(
            model_name='labsuserresult',
            name='circle_items',
            field=models.ManyToManyField(to='isle.CircleItem'),
        ),
        migrations.RunPython(fix_circle_items, reverse_code=migrations.RunPython.noop),
    ]
