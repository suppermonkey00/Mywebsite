# Generated by Django 3.1.3 on 2020-11-23 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_categoty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoty',
            new_name='category',
        ),
    ]