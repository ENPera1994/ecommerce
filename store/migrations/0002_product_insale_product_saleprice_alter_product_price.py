# Generated by Django 4.2.5 on 2024-01-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inSale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='salePrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
