# Generated by Django 4.1.6 on 2023-03-13 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'ShippingAddress', 'verbose_name_plural': 'ShippingAddresses'},
        ),
    ]
