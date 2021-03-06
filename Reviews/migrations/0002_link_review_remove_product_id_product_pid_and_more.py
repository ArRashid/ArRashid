# Generated by Django 4.0.4 on 2022-06-28 16:42

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('site', models.CharField(max_length=200)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='uploads/reviews/link')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('spec', ckeditor_uploader.fields.RichTextUploadingField()),
                ('pros', models.TextField()),
                ('cons', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='pid',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/reviews/product'),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.product'),
        ),
        migrations.AddField(
            model_name='link',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.review'),
        ),
    ]
