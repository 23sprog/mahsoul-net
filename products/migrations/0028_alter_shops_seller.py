# Generated by Django 4.2.4 on 2024-01-13 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0027_alter_shops_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='seller',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop', to=settings.AUTH_USER_MODEL, verbose_name='فروشنده'),
        ),
    ]
