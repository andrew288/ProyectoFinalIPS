# Generated by Django 3.2 on 2021-07-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0014_articulos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='posicion',
        ),
        migrations.AddField(
            model_name='articulos',
            name='autor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articulos',
            name='palabras_clave',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='art_archivo',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='titulo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
