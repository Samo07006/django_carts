# Generated by Django 4.2 on 2023-04-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='count',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Product count'),
        ),
    ]
