# Generated by Django 2.0.2 on 2018-03-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20180302_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='paysys_id',
            field=models.CharField(blank=True, max_length=64, verbose_name='номер заказа в платежной системе'),
        ),
    ]
