# Generated by Django 2.0.2 on 2018-03-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20180305_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='counter_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.CounterAgent', verbose_name='Контрагент'),
        ),
    ]