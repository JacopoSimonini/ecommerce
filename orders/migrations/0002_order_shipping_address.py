# Generated by Django 4.1.7 on 2023-05-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(default='Indirizzo di default', max_length=100),
        ),
    ]