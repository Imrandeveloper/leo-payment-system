# Generated by Django 2.0.2 on 2018-03-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_auto_20180314_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status_sber',
            field=models.PositiveSmallIntegerField(choices=[(100, '-----'), (0, 'Заказ зарегистрирован, но не оплачен'), (1, 'Предавторизованная сумма захолдирована (для двухстадийных платежей)'), (2, 'Проведена полная авторизация суммы заказа'), (3, 'Авторизация отменена'), (4, 'По транзакции была проведена операция возврата'), (5, 'Инициирована авторизация через ACS банка-эмитента'), (6, 'Авторизация отклонена')], default=100, verbose_name='Статус платежной системы'),
        ),
    ]