# Generated by Django 3.2 on 2021-07-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0007_alter_perfiles_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Foto de perfil'),
        ),
    ]