# Generated by Django 5.0.6 on 2024-06-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_ordersmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default=('Pending', 'Pending'), max_length=20),
        ),
    ]
