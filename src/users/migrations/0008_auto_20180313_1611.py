# Generated by Django 2.0.2 on 2018-03-13 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180313_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientuser',
            name='billing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Billing', verbose_name='Биллинг'),
        ),
        migrations.AlterField(
            model_name='clientuser',
            name='billing_userid',
            field=models.CharField(max_length=250, verbose_name='Идентификатор пользователя в системе биллинга'),
        ),
    ]
