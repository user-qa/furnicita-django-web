# Generated by Django 5.0.6 on 2024-05-22 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blogtagmodel_blogmodel_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogtagmodel',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.RenameField(
            model_name='blogmodel',
            old_name='tag',
            new_name='tags',
        ),
    ]
