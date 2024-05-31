# Generated by Django 5.0.6 on 2024-05-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Category Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='Category Image'),
        ),
    ]