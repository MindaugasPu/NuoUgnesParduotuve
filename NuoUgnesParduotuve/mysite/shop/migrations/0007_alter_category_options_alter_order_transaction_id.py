# Generated by Django 4.1.6 on 2023-03-09 20:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_order_customer_alter_orderline_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique transacion ID for order', verbose_name='UUID'),
        ),
    ]