# Generated by Django 5.1 on 2024-08-10 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('pending', 'Pending'), ('delivered', 'Delivered'), ('done', 'Done')], default='new', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True, db_default=datetime.datetime(2024, 8, 10, 15, 42, 44, 798915, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_default=datetime.datetime(2024, 8, 10, 15, 42, 44, 798915, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True, db_default=datetime.datetime(2024, 8, 10, 15, 42, 44, 798915, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_default=datetime.datetime(2024, 8, 10, 15, 42, 44, 798915, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
