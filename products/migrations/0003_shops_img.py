# Generated by Django 4.2.4 on 2023-10-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_img_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='img',
            field=models.ImageField(null=True, upload_to='images_shop/', verbose_name='تصویر محصول'),
        ),
    ]
