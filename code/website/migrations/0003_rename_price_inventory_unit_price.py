# Generated by Django 5.1 on 2024-08-25 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_quantity_inventory_quantity_avl_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='price',
            new_name='unit_price',
        ),
    ]
