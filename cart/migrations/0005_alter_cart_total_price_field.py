# Generated by Django 4.1.7 on 2023-05-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_total_price_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price_field',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
    ]
