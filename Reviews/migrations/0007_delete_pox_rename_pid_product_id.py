# Generated by Django 4.0.4 on 2022-07-03 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0006_pox'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pox',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pid',
            new_name='id',
        ),
    ]