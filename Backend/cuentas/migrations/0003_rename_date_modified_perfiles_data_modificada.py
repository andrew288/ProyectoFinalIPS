# Generated by Django 3.2 on 2021-06-06 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_publicaciones_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfiles',
            old_name='date_modified',
            new_name='data_modificada',
        ),
    ]