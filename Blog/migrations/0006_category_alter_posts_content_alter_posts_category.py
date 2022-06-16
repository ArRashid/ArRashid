# Generated by Django 4.0.4 on 2022-06-13 19:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_posts_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.category'),
        ),
    ]