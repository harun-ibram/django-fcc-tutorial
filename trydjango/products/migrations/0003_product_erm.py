# Generated by Django 5.0.2 on 2024-02-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_active_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='erm',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
