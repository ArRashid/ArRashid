# Generated by Django 4.0.4 on 2022-06-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_posts_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/blog/posts'),
        ),
    ]