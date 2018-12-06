# Generated by Django 2.1.4 on 2018-12-06 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=12)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('cpf', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=15)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=4)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='clients_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clientes.Pessoa')),
                ('instituicao', models.CharField(max_length=50)),
            ],
            bases=('clientes.pessoa',),
        ),
    ]
