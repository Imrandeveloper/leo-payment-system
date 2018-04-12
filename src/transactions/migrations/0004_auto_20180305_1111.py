# Generated by Django 2.0.2 on 2018-03-05 11:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20180302_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_passed',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='is_success',
        ),
        migrations.AddField(
            model_name='transaction',
            name='final_url',
            field=models.URLField(default='', verbose_name='url для редиректа после потверждения оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='service_id',
            field=models.PositiveIntegerField(default=0, verbose_name='ID услуги'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Новая'), (1, 'Создана'), (2, 'Проведена'), (3, 'Успешна'), (4, 'Возвращена')], default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='gateway_response',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='данные ответа платежного шлюза'),
        ),
    ]
