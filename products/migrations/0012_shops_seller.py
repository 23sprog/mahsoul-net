# Generated by Django 4.2.4 on 2023-11-01 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0011_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='seller',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='فروشنده'),
        ),
    ]
