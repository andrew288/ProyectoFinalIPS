# Generated by Django 3.2 on 2021-07-16 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0009_alter_perfiles_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
    ]