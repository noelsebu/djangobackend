# Generated by Django 3.0.2 on 2020-02-24 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_product_supplier_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier_id',
        ),
    ]
