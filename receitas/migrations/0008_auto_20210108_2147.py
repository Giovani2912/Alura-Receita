# Generated by Django 3.1.3 on 2021-01-09 00:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0007_auto_20210108_2144'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cozinheiro',
            new_name='Receita',
        ),
    ]