# Generated by Django 2.1.4 on 2019-01-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0020_auto_20190114_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=473108, max_length=14, null=True),
        ),
    ]