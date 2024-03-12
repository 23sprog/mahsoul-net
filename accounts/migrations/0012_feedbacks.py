# Generated by Django 4.2.4 on 2023-12-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_tickets_responced_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='نام')),
                ('description', models.TextField(verbose_name='متن بازخورد')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'بازخورد',
                'verbose_name_plural': 'بازخورد ها',
                'ordering': ('created_at',),
            },
        ),
    ]
