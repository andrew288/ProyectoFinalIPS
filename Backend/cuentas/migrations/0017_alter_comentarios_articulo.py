# Generated by Django 3.2 on 2021-07-26 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0016_auto_20210726_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cuentas.articulos'),
        ),
    ]