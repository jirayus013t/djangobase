# Generated by Django 2.2.17 on 2020-11-11 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='products_image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='products_price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='products_qty',
            new_name='product_qty',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='products_status',
            new_name='product_status',
        ),
    ]