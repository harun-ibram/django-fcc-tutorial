# Generated by Django 5.0.2 on 2024-02-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_erm'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
