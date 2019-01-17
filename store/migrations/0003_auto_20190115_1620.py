# Generated by Django 2.1.5 on 2019-01-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
