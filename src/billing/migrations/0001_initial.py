# Generated by Django 2.0.2 on 2018-03-01 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название')),
                ('url', models.URLField(blank=True, verbose_name='url биллинга')),
            ],
            options={
                'verbose_name': 'биллинг',
                'verbose_name_plural': 'биллинги',
            },
        ),
        migrations.CreateModel(
            name='CounterAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название')),
            ],
            options={
                'verbose_name': 'контрагент',
                'verbose_name_plural': 'контрагенты',
            },
        ),
        migrations.AddField(
            model_name='billing',
            name='counter_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.CounterAgent', verbose_name='контрагент'),
        ),
    ]
