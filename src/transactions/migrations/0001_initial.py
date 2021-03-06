# Generated by Django 2.0.2 on 2018-03-01 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='время проведения')),
                ('amount', models.IntegerField(verbose_name='сумма')),
                ('paysys_id', models.CharField(max_length=64, verbose_name='номер заказа в платежной системе')),
                ('is_success', models.BooleanField(default=False, verbose_name='успешность ответа платежного шлюза')),
                ('is_passed', models.BooleanField(default=False, verbose_name='успешность проведения')),
                ('gateway_response', models.CharField(blank=True, max_length=512, verbose_name='данные ответа платежного шлюза')),
                ('client_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.ClientUser', verbose_name='плательщик')),
            ],
            options={
                'verbose_name': 'транзакция',
                'verbose_name_plural': 'транзакции',
            },
        ),
    ]
