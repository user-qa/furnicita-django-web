# Generated by Django 5.0.6 on 2024-05-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagmodel',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='sku',
            field=models.CharField(max_length=20),
        ),
    ]
