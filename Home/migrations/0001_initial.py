# Generated by Django 4.0.4 on 2022-06-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppsMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('details', models.CharField(max_length=100)),
                ('link', models.CharField(default='www.google.com', max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='uploads/icons/features')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('imga', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
