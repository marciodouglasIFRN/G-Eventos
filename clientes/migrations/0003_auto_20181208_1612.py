# Generated by Django 2.1.4 on 2018-12-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20181208_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(default=391424, max_length=14),
        ),
    ]
