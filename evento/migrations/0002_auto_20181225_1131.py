# Generated by Django 2.1.4 on 2018-12-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='meida/eventos_photos'),
        ),
    ]