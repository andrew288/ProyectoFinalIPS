# Generated by Django 3.2 on 2021-07-26 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuentas', '0018_rename_text_comentarios_comentario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comentarios',
            new_name='Comentarios_publicacion',
        ),
        migrations.CreateModel(
            name='Comentarios_articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cuentas.perfiles')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cuentas.publicaciones')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='cuentas.comentarios_articulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]