# Generated by Django 5.0.2 on 2024-02-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.TextField(blank=True),
        ),
    ]