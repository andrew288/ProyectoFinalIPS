# Generated by Django 3.2 on 2021-07-26 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0013_delete_articulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('pub_fecha', models.DateField(null=True)),
                ('resumen', models.TextField(null=True)),
                ('art_archivo', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('posicion', models.CharField(choices=[('HM', 'HOME_MAIN'), ('BM', 'BOTTOM_MAIN'), ('TM', 'TOP_MAIN')], default='TM', max_length=50)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cuentas.categorias')),
            ],
        ),
    ]
