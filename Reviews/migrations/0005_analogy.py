# Generated by Django 4.0.4 on 2022-07-01 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0004_alter_product_cover_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analogy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=25)),
                ('percent', models.IntegerField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.product')),
            ],
        ),
    ]