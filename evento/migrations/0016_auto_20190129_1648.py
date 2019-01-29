# Generated by Django 2.1.4 on 2019-01-29 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0015_evento_hora_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='categoria',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_evento',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
