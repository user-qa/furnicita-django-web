# Generated by Django 5.0.6 on 2024-05-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_tagmodel_options_alter_productsmodel_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=11, max_digits=10),
            preserve_default=False,
        ),
    ]
