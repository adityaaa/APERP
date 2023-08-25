# Generated by Django 3.2.20 on 2023-08-25 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiry_date', models.DateField()),
                ('pack', models.CharField(max_length=50)),
                ('batch', models.CharField(default='', max_length=50)),
                ('rate', models.DecimalField(decimal_places=2, default='', max_digits=10)),
                ('hsn', models.CharField(default='', max_length=10)),
                ('sgst', models.DecimalField(decimal_places=2, default=12.0, max_digits=10)),
                ('cgst', models.DecimalField(decimal_places=2, default=12.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('full_address', models.TextField(default='')),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('drug_license_number', models.CharField(default='', max_length=50)),
                ('gstin_number', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=100)),
                ('bill_number', models.CharField(max_length=10, unique=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack', models.CharField(max_length=50)),
                ('batch', models.CharField(default='', max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('free', models.PositiveIntegerField(default=0)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sgst', models.DecimalField(decimal_places=2, default=12.0, max_digits=10)),
                ('cgst', models.DecimalField(decimal_places=2, default=12.0, max_digits=10)),
                ('hsn', models.CharField(default='', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.inventoryitem')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.sale')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Tablet', 'Tablet'), ('Syrup', 'Syrup'), ('Capsule', 'Capsule')], max_length=20)),
                ('expiry_date', models.DateField(default='2023-01-01')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_app.manufacturer'),
        ),
    ]