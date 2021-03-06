# Generated by Django 2.0.7 on 2019-10-22 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isle', '0058_auto_20191011_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='DpTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50, unique=True)),
                ('title', models.TextField()),
                ('models', models.ManyToManyField(related_name='tools', to='isle.MetaModel')),
            ],
        ),
        migrations.CreateModel(
            name='DPType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ModelCompetence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='isle.DpCompetence')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competences', to='isle.MetaModel')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isle.DPType')),
            ],
        ),
        migrations.AddField(
            model_name='circleitem',
            name='created_in',
            field=models.CharField(default='labs', max_length=15),
        ),
        migrations.AddField(
            model_name='circleitem',
            name='source',
            field=models.CharField(default='labs', max_length=15),
        ),
        migrations.AlterUniqueTogether(
            name='modelcompetence',
            unique_together={('model', 'competence')},
        ),
    ]
