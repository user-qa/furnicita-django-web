# Generated by Django 5.0.6 on 2024-06-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_ordersmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=20),
        ),
    ]
