# Generated by Django 2.0.2 on 2018-03-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_auto_20180312_0843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Транзакция', 'verbose_name_plural': 'Транзакции'},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Новая'), (1, 'Создана'), (2, 'Успешна'), (3, 'Ошибка/Возврат')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status_sber',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Заказ зарегистрирован, но не оплачен'), (1, 'Предавторизованная сумма захолдирована (для двухстадийных платежей)'), (2, 'Проведена полная авторизация суммы заказа'), (3, 'Авторизация отменена'), (4, 'По транзакции была проведена операция возврата'), (5, 'Инициирована авторизация через ACS банка-эмитента'), (6, 'Авторизация отклонена')], default=-1, verbose_name='Статус платежной системы'),
        ),
    ]
