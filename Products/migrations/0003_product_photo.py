# Generated by Django 4.2.3 on 2023-10-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_shelf_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]