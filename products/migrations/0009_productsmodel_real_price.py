# Generated by Django 5.0.6 on 2024-06-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_productsmodel_long_detail_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='real_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
