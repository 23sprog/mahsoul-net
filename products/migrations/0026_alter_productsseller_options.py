# Generated by Django 4.2.4 on 2023-12-12 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_delete_tickets'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsseller',
            options={'ordering': ('created_at',), 'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبد های خرید'},
        ),
    ]
