# Generated by Django 3.1.1 on 2020-10-06 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201004_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cutomer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='cutomer',
            new_name='customer',
        ),
    ]
