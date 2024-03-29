# Generated by Django 4.2.4 on 2023-11-02 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0014_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('created_at',), 'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.CreateModel(
            name='ProductsSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('b', 'buying'), ('s', 'sold')], default='b', max_length=1, verbose_name='وضعیت سفارش')),
                ('count', models.IntegerField(max_length=50, verbose_name='تعداد کالا')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.products', verbose_name='کالا')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='خریدار')),
            ],
        ),
    ]
