# Generated by Django 2.0.2 on 2018-03-13 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_staffuser_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientuser',
            options={'verbose_name': 'Плательщик', 'verbose_name_plural': 'Плательщики'},
        ),
    ]