# Generated by Django 4.2.5 on 2023-10-01 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_orderproduct_variation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='is_ordered',
            new_name='ordered',
        ),
    ]