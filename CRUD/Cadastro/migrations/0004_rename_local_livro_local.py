# Generated by Django 3.2.9 on 2021-12-08 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0003_auto_20211208_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='Local',
            new_name='local',
        ),
    ]
