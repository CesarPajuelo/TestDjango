# Generated by Django 3.2.5 on 2021-07-14 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_trabajo_nuevo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajo',
            name='descripcion',
        ),
    ]
