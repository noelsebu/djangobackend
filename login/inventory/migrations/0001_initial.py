# Generated by Django 3.0.2 on 2020-02-19 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=100)),
                ('line2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenum', models.IntegerField(max_length=10)),
                ('date_joined', models.DateField()),
                ('date_last_purchase', models.DateField()),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Address')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_description', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrp', models.FloatField()),
                ('wsp', models.FloatField()),
                ('quantity', models.IntegerField(default=0)),
                ('parent_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('date_joined', models.DateField()),
                ('other_details', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_details', models.CharField(max_length=100)),
                ('outstanding_amt', models.FloatField(default=0)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Address')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('other_details', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Customers')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Staff')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Supplier')),
                ('transaction_type_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.TransactionType')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField()),
                ('document_text', models.CharField(max_length=100)),
                ('other_details', models.CharField(max_length=100)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.DocumentType')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Transaction')),
            ],
        ),
    ]
