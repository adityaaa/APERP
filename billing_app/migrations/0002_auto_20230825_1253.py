# Generated by Django 3.2.20 on 2023-08-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saledetail',
            name='product',
        ),
        migrations.RemoveField(
            model_name='saledetail',
            name='sale',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='pack',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='SaleDetail',
        ),
    ]