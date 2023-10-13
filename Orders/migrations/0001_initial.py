# Generated by Django 4.2.3 on 2023-10-09 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Total', models.IntegerField(default=100)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Pending', max_length=200)),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
        ),
    ]