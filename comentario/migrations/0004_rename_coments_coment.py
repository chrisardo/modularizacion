# Generated by Django 4.2.5 on 2023-09-29 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0003_coments_signature'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coments',
            new_name='Coment',
        ),
    ]