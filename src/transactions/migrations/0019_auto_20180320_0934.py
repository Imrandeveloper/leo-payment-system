# Generated by Django 2.0.2 on 2018-03-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_auto_20180319_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='service_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID услуги'),
        ),
    ]
